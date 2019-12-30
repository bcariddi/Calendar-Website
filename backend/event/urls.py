from django.urls import path
from . import views

urlpatterns = [
	path('all', views.allEvents),
	path('new/<int:orgID>', views.add),
	path('<int:id>', views.event),
	path('update/<int:id>', views.update),
	path('delete/<int:id>', views.delete),
]