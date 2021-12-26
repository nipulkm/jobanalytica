from django.urls import path
from apps.company import views

urlpatterns = [
	path('company/registration/', views.companyRegistration, name='companyRegistration'),
	path('company/login/', views.companyLogin, name='companyLogin'),
	path('company/logout/', views.companyLogout, name='companyLogout'),
	path('company/dashboard/', views.companyDashboard, name='companyDashboard'),
	path('company/dashboard/createjobpost/', views.jobPostCreate, name='jobPostCreate'),
]
