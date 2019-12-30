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

def events(request):
	if request.method == "GET":	
		sortBy = request.GET.get('sortBy','-startDate')
		count = request.GET.get('count',None)
	
		# How Many Events to Return
		if count != None:
			eventsList = Event.objects.order_by(sortBy)[:int(count)]
		else:
			eventsList = Event.objects.order_by(sortBy)
			
		eventsList = '[' + ', '.join([str(event) for event in eventsList]) + ']'
		
		return HttpResponse(eventsList, content_type="application/json")

			
def add(request):
	if request.method == "GET":
		form = EventForm()
		
		csrf_token = get_token(request)
		csrf_token_html = '<input type="hidden" name="csrfmiddlewaretoken" value="{}" />'.format(csrf_token)

		return HttpResponse("<form method='post'>" + form.as_ul() + csrf_token_html + "<input type='submit'></form>")
		
	elif request.method == "POST":
		# TODO: Do some validation
		form = EventForm(request.POST)
	
		if form.is_valid():
			form.save()
			return HttpResponse("Success")
		else:
			return HttpResponse("Fail")
    
def update(request, id):
	updatingEvent = Event.objects.filter(id=id)
				
	if len(updatingEvent) > 0:
		updatingEvent = updatingEvent[0]
		
		if request.method == "GET":		
			form = EventForm(instance=updatingEvent)
		
			csrf_token = get_token(request)
			csrf_token_html = '<input type="hidden" name="csrfmiddlewaretoken" value="{}" />'.format(csrf_token)

			return HttpResponse("<form method='post'>" + form.as_ul() + csrf_token_html + "<input type='submit'></form>")
			
		elif request.method == "POST":
			form = EventForm(request.POST, instance=updatingEvent)
			form.save()
			return HttpResponse("Success")

	return HttpResponse("No Event Found")


def delete(request, id):
	# TODO: Do Some validation	
	deletingEvent = Event.objects.filter(id=id)
	
	if len(deletingEvent) > 0:
		deletingEvent.delete()
		return HttpResponse("Success")
	
	return HttpResponse("Fail")
	