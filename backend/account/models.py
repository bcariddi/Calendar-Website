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
	
	def __str__(self):
		# Returns a JSON representation
		studentJSON = {}
		studentJSON["id"] = self.id
		studentJSON["username"] = self.user.username
		studentJSON["email"] = self.user.email
		studentJSON["firstName"] = self.user.first_name
		studentJSON["lastName"] = self.user.last_name
		
		studentJSON["savedEvents"] = list(map(lambda x: x.id, self.savedEvents.all()))
		studentJSON["organizations"] = list(map(lambda x: x.id, self.organizations.all()))
		studentJSON["following"] = list(map(lambda x: x.id, self.following.all()))
		
		return json.dumps(studentJSON)
	
class LoginForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username','password']
		