from django.urls import path
from . import views

urlpatterns = [
	path('', views.events),
	path('new', views.add),
	path('update/<int:id>', views.update),
	path('delete/<int:id>', views.delete)
]