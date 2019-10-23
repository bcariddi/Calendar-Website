from django.db import models
from django.contrib.postgres import fields
from django import forms
import json, datetime

class Event(models.Model):		
	# Basic Info
	title = models.CharField(default='',max_length=200)
	location = models.CharField(default='',max_length=200)
	eventDescription = models.TextField(default='',max_length=650)
	
	# Time Information
	startDate = models.DateTimeField(default=None)
	endDate = models.DateTimeField(default=None)
	
	#Tags Array
	eventTags = fields.ArrayField(models.CharField(default='', max_length=50),default=list())
	
	# More Metadata
	
	## Event Creator
	owner = models.CharField(default='',max_length=100)
	
	## Capacity
	capacity = models.PositiveIntegerField(default=0)
	
	
	def __str__(self):
		# Returns a JSON representation
		eventJSON = {}
		eventJSON["title"] = self.title
		eventJSON["location"] = self.location
		eventJSON["description"] = self.eventDescription
		
		eventJSON["startDate"] = self.startDate.isoformat()
		eventJSON["endDate"] = self.endDate.isoformat()
		
		eventJSON["tags"] = self.eventTags
		
		eventJSON["owner"] = self.owner
		eventJSON["capacity"] = self.capacity
		
		
		return json.dumps(eventJSON)
		
class EventForm(forms.Form):
		# Basic Info
	title = forms.CharField(default='',max_length=200)
	location = forms.CharField(default='',max_length=200)
	eventDescription = forms.TextField(default='',max_length=650)
	
	# Time Information
	startDate = forms.DateTimeField(default=None)
	endDate = forms.DateTimeField(default=None)
	
	#Tags Array (FIND A BETTER DATATYPE)
	eventTags = forms.CharField(default='',max_length=600)
	
	# More Metadata
	
	## Event Creator
	owner = forms.CharField(default='',max_length=100)
	
	## Capacity
	capacity = forms
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	 z.PositiveIntegerField(default=0)