from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import get_token
from django.contrib.auth.decorators import login_required

from .models import Student,LoginForm
from event.models import Event
from organization.models import Organization
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Login and Logout
def loginUser(request):
	if request.method == "GET":
		form = LoginForm()
		
		csrf_token = get_token(request)
		csrf_token_html = '<input type="hidden" name="csrfmiddlewaretoken" value="{}" />'.format(csrf_token)

		return HttpResponse("<form method='post'>" + form.as_ul() + csrf_token_html + "<input type='submit'></form>")
	else:
		username = request.POST["username"]
		password = request.POST["password"]
	
		user = authenticate(request, username=username,password=password)

		if user != None:
			login(request,user)
			return HttpResponse("Success")
		
	return HttpResponse("Fail")
	
def logoutUser(request):
	logout(request)
	return HttpResponse("Success")

# Find User
def findUser(request, username):
	if request.method == "GET":
		user = User.objects.filter(username=username)
		
		if len(user) > 0:
			return HttpResponse(user[0].student, content_type="application/json")
		

# User Actions	
@login_required(login_url="/")
def saveEvent(request):
	id = request.GET.get("id",None)
	
	if id != None:
		savingEvent = Event.objects.filter(id=id)
		
		if len(savingEvent) > 0:
			savingEvent = savingEvent[0]
			
			request.user.student.savedEvents.add(savingEvent)
			return HttpResponse("Success")
	
	return HttpResponse("Fail")
	
@login_required(login_url="/")
def unsaveEvent(request):
	id = request.GET.get("id",None)
	
	if id != None:
		savingEvent = Event.objects.filter(id=id)
		
		if len(savingEvent) > 0:
			savingEvent = savingEvent[0]
			
			request.user.student.savedEvents.remove(savingEvent)
			return HttpResponse("Success")
	
	return HttpResponse("Fail")

@login_required(login_url="/")
def followOrg(request):
	id = request.GET.get("id",None)
	
	if id != None:
		savingOrg = Organization.objects.filter(id=id)
		
		if len(savingOrg) > 0:			
			request.user.student.following.add(savingOrg[0])
			return HttpResponse("Success")
	
	return HttpResponse("Fail")
	
def unfollowOrg(request):
	id = request.GET.get("id",None)
	
	if id != None:
		savingOrg = Organization.objects.filter(id=id)
		
		if len(savingOrg) > 0:			
			request.user.student.following.remove(savingOrg[0])
			return HttpResponse("Success")
	
	return HttpResponse("Fail")

# Admin Actions
def createUser(request):
	if request.method == "GET":
		form = UserCreationForm()
		
		csrf_token = get_token(request)
		csrf_token_html = '<input type="hidden" name="csrfmiddlewaretoken" value="{}" />'.format(csrf_token)

		return HttpResponse("<form method='post'>" + form.as_ul() + csrf_token_html + "<input type='submit'></form>")
		
	elif request.method == "POST":
		form = UserCreationForm(request.POST)
	
		if form.is_valid():
			user = form.save()
			student = Student.objects.create(user=user)
			return HttpResponse("Success")

	return HttpResponse("Fail")
		
def deleteUser(request,id):
	deletingUser = Student.objects.filter(id=id)
	
	if len(deletingUser) > 0:
		deletingUser.delete()
		return HttpResponse("Success")
	
	return HttpResponse("Fail")
	
		
	