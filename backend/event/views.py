from django.shortcuts import render
from django.http import HttpResponse

from .models import Event
# Create your views here.

def events(req):
	sortBy = req.GET.get('sortBy','-startDate')
	count = req.GET.get('count',None)
	
	if count is not None:
		eventsList = Event.objects.order_by(sortBy)[:int(count)]
	else:
		eventsList = Event.objects.order_by(sortBy)

	return HttpResponse(eventsList, content_type="application/json")