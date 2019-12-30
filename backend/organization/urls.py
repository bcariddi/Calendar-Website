from django.urls import path
from . import views

urlpatterns = [
	path('all', views.allOrgs),
	path('<int:id>', views.organization),
	path('create', views.createOrg),
]