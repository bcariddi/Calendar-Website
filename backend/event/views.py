from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import get_token
from django.contrib.auth.decorators import login_required
import json

from .models import Event,EventForm
from organization.models import Organization

def allEvents(request):
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

def event(request, id):
	if request.method == "GET":	
		event = Event.objects.filter(id=id)
		
		if len(event) > 0:
			return HttpResponse(event[0], content_type="application/json")

def add(request, orgID):
	if request.method == "GET":
		form = EventForm()
		
		csrf_token = get_token(request)
		csrf_token_html = '<input type="hidden" name="csrfmiddlewaretoken" value="{}" />'.format(csrf_token)

		return HttpResponse("<form method='post'>" + form.as_ul() + csrf_token_html + "<input type='submit'></form>")
		
	elif request.method == "POST":
		# TODO: Do some validation
		form = EventForm(request.POST)
	
		if form.is_valid():
			organization = Organization.objects.filter(id=orgID)
			
			if len(organization) > 0:
				organization = organization[0]
				
				if organization in request.user.student.organizations.all():
					event = form.save()
					event.owner = request.user.username
					event.save()
					event.organizations.add(organization)
			
					return HttpResponse("Success")

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
			
			for organization in form.organizations.all():
				if organization in request.user.student.organizations.all():
					form.save()
					return HttpResponse("Success")

	return HttpResponse("No Event Found")


def delete(request, id):
	# TODO: Do Some validation	
	deletingEvent = Event.objects.filter(id=id)
	
	if len(deletingEvent) > 0:
		for organization in deletingEvent[0].organizations.all():
			if organization in request.user.student.organizations.all():
				deletingEvent.delete()
				return HttpResponse("Success")
	
	return HttpResponse("Fail")
	