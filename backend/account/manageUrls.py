from django.urls import path
from . import views

urlpatterns = [
	path('admin/create',views.createUser),
	path('admin/delete/<int:id>',views.deleteUser),
]