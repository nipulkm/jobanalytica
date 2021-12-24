from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from library import errormessage
from library import constants as const, decorator
from apps.candidate.models import UserRole
from apps.company.forms import CompanyRegistrationForm
from apps.candidate.forms import LoginForm
from apps.company.controller import companyregistrationcontroller, companylogincontroller

def companyRegistration(request):
	if request.method == 'GET':
		form = CompanyRegistrationForm()
		context = {const.COMPANY_REGISTRATION_FORM: form}
		try:
			return render(request, 'company/companyRegistration.html', context)
		except:
			messages.error(request, errormessage.INTERNAL_SERVER_ERROR)
			return render(request, 'company/companyRegistration.html', context)
	if request.method == 'POST':
		try:
			validation = companyregistrationcontroller.companyRegistrationFormValidation(request)
			if validation.isValid == True:
				return redirect('/company/login/')
			return render(request, 'company/companyRegistration.html', validation.response)
		except:
			form = CompanyRegistrationForm(request.POST)
			context = {const.COMPANY_REGISTRATION_FORM: form}
			messages.error(request, errormessage.INTERNAL_SERVER_ERROR)
			return render(request, 'company/companyRegistration.html', context)

@decorator.unauthenticated_user
def companyLogin(request):
	form = LoginForm()
	context = {
		const.LOGIN_FORM_PROPERTY: form,
		"userRole": "Company"
	}
	if request.method == 'GET':
		try:
			return render(request, 'login.html', context)
		except:
			messages.error(request, errormessage.INTERNAL_SERVER_ERROR)
			return render(request, 'login.html', context)
	if request.method == 'POST':
		try:
			validation = companylogincontroller.loginFormValidation(request)
			if validation.isValid == True:
				return redirect('/company/dashboard/')
			return render(request, 'login.html', validation.response)
		except:
			messages.error(request, errormessage.INTERNAL_SERVER_ERROR)
			return render(request, 'login.html', context)

# @rolePermission([UserRole.objects.get(roleName='Company')])
#@decorator.unauthenticated_user
@login_required(login_url="/company/login/")
@decorator.allowed_users(allowed_roles=['Company'])
def companyDashboard(request):
	if request.method == 'GET':
		context = {
			"isLogged": True,
			"userRole": "Company"
		}
		return render(request, 'company/companyDashboard.html', context)

@login_required(login_url="/company/login/")
@decorator.allowed_users(allowed_roles=['Company'])
def companyLogout(request):
	logout(request)
	return redirect('/home')
