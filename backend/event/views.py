from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import get_token
import json

from .models import Event,EventForm

'''
# API Syntax 
## Events
* /events/
	* sortBy
	* count
* /events/delete
	* id

'''

def events(req):
	if req.method == "GET":	
		sortBy = req.GET.get('sortBy','-startDate')
		count = req.GET.get('count',None)
	
		# How Many Events to Return
		if count != None:
			eventsList = Event.objects.order_by(sortBy)[:int(count)]
		else:
			eventsList = Event.objects.order_by(sortBy)
			
		eventsList = '[' + ', '.join([str(event) for event in eventsList]) + ']'
		
		return HttpResponse(eventsList, content_type="application/json")

			
def add(req):
	if req.method == "GET":
		form = EventForm()
		
		csrf_token = get_token(req)
		csrf_token_html = '<input type="hidden" name="csrfmiddlewaretoken" value="{}" />'.format(csrf_token)

		return HttpResponse("<form method='post'>" + form.as_ul() + csrf_token_html + "<input type='submit'></form>")
		
	elif req.method == "POST":
		# TODO: Do some validation
		form = EventForm(req.POST)
	
		if form.is_valid():
			title = form.cleaned_data["title"]
			location = form.cleaned_data["location"]
			description = form.cleaned_data["description"]
			startDate = form.cleaned_data["startDate"]
			endDate = form.cleaned_data["endDate"]
			tags = form.cleaned_data["tags"]
			owner = form.cleaned_data["owner"]
			capacity = form.cleaned_data["capacity"]
			
			newEvent = Event.objects.create(
				title = title,
				location = location,
				description = description,
				startDate = startDate,
				endDate = endDate,
				tags = tags,
				owner = owner,
				capacity = capacity
			)
			
			return HttpResponse("Success")
		else:
			return HttpResponse("Fail")
    
def update(req, id):
	updatingEvent = Event.objects.filter(id=id)
				
	if len(updatingEvent) > 0:
		updatingEvent = updatingEvent[0]
		
		if req.method == "GET":		
			form = EventForm(instance=updatingEvent)
		
			csrf_token = get_token(req)
			csrf_token_html = '<input type="hidden" name="csrfmiddlewaretoken" value="{}" />'.format(csrf_token)

			return HttpResponse("<form method='post'>" + form.as_ul() + csrf_token_html + "<input type='submit'></form>")
			
		elif req.method == "POST":
			form = EventForm(req.POST, instance=updatingEvent)
			form.save()
			return HttpResponse("Success")

	return HttpResponse("No Event Found")


def delete(req, id):
	# TODO: Do Some validation	
	deletingEvent = Event.objects.filter(id=id)
	
	if len(deletingEvent) > 0:
		deletingEvent.delete()
		return HttpResponse("Success")
	
	return HttpResponse("Fail")
	