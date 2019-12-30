from django.db import models
from django.contrib.postgres import fields
from django import forms
import json, datetime, enum

class Tag(enum.Enum):
	NONE = 0
	FREE_FOOD = 1
	

class Event(models.Model):		
	# Basic Info
	title = models.CharField(default='',max_length=200)
	location = models.CharField(default='',max_length=200)
	description = models.TextField(default='',max_length=650)
	
	# Time Information
	startDate = models.DateTimeField(default=None)
	endDate = models.DateTimeField(default=None)
	
	#Tags Array
	tags = fields.ArrayField(models.PositiveIntegerField(),default=list)
	
	# More Metadata
	
	## Event Creator
	owner = models.CharField(default='',max_length=100)
	
	## Capacity
	capacity = models.PositiveIntegerField(default=0)
	
	class Meta:
		ordering = ["startDate"]
		
	def __str__(self):
		# Returns a JSON representation
		eventJSON = {}
		eventJSON["id"] = self.id
		eventJSON["title"] = self.title
		eventJSON["location"] = self.location
		eventJSON["description"] = self.description
		
		eventJSON["startDate"] = self.startDate.isoformat()
		eventJSON["endDate"] = self.endDate.isoformat()
		
		eventJSON["tags"] = self.tags
		
		eventJSON["owner"] = self.owner
		eventJSON["capacity"] = self.capacity
		
		
		return json.dumps(eventJSON)
		
# Forms
class EventForm(forms.ModelForm):
	class Meta:
		model = Event
		fields = ["title", "location", "description", "startDate", "endDate", "tags", "owner", "capacity"]