from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import get_token
import json

from .models import Organization, OrganizationForm

def allOrgs(request):
	if request.method == "GET":	
		sortBy = request.GET.get('sortBy','title')
		count = request.GET.get('count',None)
	
		# How Many Events to Return
		if count != None:
			orgList = Organization.objects.order_by(sortBy)[:int(count)]
		else:
			orgList = Organization.objects.order_by(sortBy)
			
		orgList = '[' + ', '.join([str(org) for org in orgList]) + ']'
		
		return HttpResponse(orgList, content_type="application/json")
		
def organization(request, id):
	if request.method == "GET":	
		org = Organization.objects.filter(id=id)
		
		if len(org) > 0:
			return HttpResponse(org[0], content_type="application/json")

def createOrg(request):
	if request.method == "GET":
		form = OrganizationForm()
		
		csrf_token = get_token(request)
		csrf_token_html = '<input type="hidden" name="csrfmiddlewaretoken" value="{}" />'.format(csrf_token)

		return HttpResponse("<form method='post'>" + form.as_ul() + csrf_token_html + "<input type='submit'></form>")
		
	elif request.method == "POST":
		# TODO: Do some validation
		form = OrganizationForm(request.POST)
	
		if form.is_valid():
			form.save()
			return HttpResponse("Success")
		else:
			return HttpResponse("Fail")
