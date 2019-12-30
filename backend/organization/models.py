from django.db import models
from django.contrib.postgres import fields
from django import forms
import json, datetime, enum

from event.models import Event
from account.models import Student

class Category(enum.Enum):
	NONE = 0
	SPORTS = 1
	SERVICE = 2

class Organization(models.Model):
	name = models.CharField(default='',max_length=200)
	description = models.TextField(default='',max_length=650)
	
	categories = fields.ArrayField(models.PositiveIntegerField(),default=list)
	
	officers = models.ManyToManyField(Student, related_name="organizations")
	followers = models.ManyToManyField(Student,related_name="following", blank=True)
	events = models.ManyToManyField(Event,related_name="organizations", blank=True)
	