from django.urls import path
from apps.candidate import views

urlpatterns = [
	path('home/', views.home, name='home'),
	path('candidate/registration/', views.candidateRegistration, name='candidateRegistration'),
	path('candidate/login/', views.candidateLogin, name='candidateLogin'),
]
