from django.db import models
import json, datetime

class Event(models.Model):
	# ID
	#id = models.UUIDField(primary_key=True, editable=False)
		
	# Basic Info
	title = models.CharField(max_length=200)
	location = models.CharField(max_length=200)
	description = models.TextField(default='')
	
	# Time Information
	startDate = models.DateTimeField()
	endDate = models.DateTimeField()
	
	#Tags Array
	tags = models.CharField(max_length=200,default='')#models.ArrayField(models.CharField(max_length=50))
	
	# More Metadata
	
	## Event Creator
	owner = models.CharField(max_length=100)
	
	## Capacity
	capacity = models.PositiveIntegerField(default=0)
	
	
	def __str__(self):
		# Returns a JSON representation
		eventJSON = {}
		eventJSON["title"] = self.title
		eventJSON["location"] = self.location
		eventJSON["description"] = self.description
		
		eventJSON["startDate"] = self.startDate.isoformat()
		eventJSON["endDate"] = self.endDate.isoformat()
		
		eventJSON["tags"] = self.tags.split(",")
		
		eventJSON["owner"] = self.owner
		eventJSON["capacity"] = self.capacity
		
		
		return json.dumps(eventJSON)