from django.db import models
from django.contrib.postgres import fields
from django import forms
import json, enum

from django.contrib.auth.models import User
from event.models import Event

# Create your models here.
class Student(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	
	savedEvents = models.ManyToManyField(Event, related_name="followers",blank=True)
	
	# "following" for orgs the student is in 
	# "organizations" for orgs the student manages
	
class LoginForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username','password']
		