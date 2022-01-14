from django.urls import path
from apps.resume import views

urlpatterns = [
	path('resume/create/', views.createResume, name='createResume'),
	#path('resume/view/', views.viewResume, name='viewResume')
]
