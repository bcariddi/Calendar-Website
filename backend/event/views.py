from django.shortcuts import render
from django.http import HttpResponse
import json

from .models import Event
# Create your views here.

def events(req):
	if req.method == "GET":	
		sortBy = req.GET.get('sortBy','-startDate')
		count = req.GET.get('count',None)
	
		if count is not None:
			eventsList = Event.objects.order_by(sortBy)[:int(count)]
		else:
			eventsList = Event.objects.order_by(sortBy)
			
		eventsList = '{' + ', '.join([str(event) for event in eventsList]) + '}'
	
		return HttpResponse(eventsList, content_type="application/json")

	elif req.method == "POST":
		return 