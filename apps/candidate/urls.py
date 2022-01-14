from django.urls import path
from apps.candidate import views

urlpatterns = [
	path('home/', views.home, name='home'),
	path('candidate/registration/', views.candidateRegistration, name='candidateRegistration'),
	path('candidate/login/', views.candidateLogin, name='candidateLogin'),
	path('candidate/profile/', views.profile, name='profile'),
	path('candidate/dashboard/', views.dashboard, name='dashboard'),
	path('candidate/logout/', views.candidateLogout, name='candidateLogout'),
	path('apply/<uuid:jobId>/', views.applyJob, name='applyJob'),
]
