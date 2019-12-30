from django.urls import path
from . import views

urlpatterns = [
	path('login', views.loginUser),
	path('logout', views.logoutUser),
	path('save', views.saveEvent),
	path('unsave', views.unsaveEvent),
	path('follow', views.followOrg),
	path('unfollow', views.unfollowOrg),
	path('admin/create',views.createUser),
	path('admin/delete/<int:id>',views.deleteUser),
]