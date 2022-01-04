from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from library import errormessage
from library import constants as const, decorator
from apps.candidate.models import UserRole
from apps.company.forms import CompanyRegistrationForm, JobPostForm
from apps.candidate.forms import LoginForm
from apps.company.controller import companyregistrationcontroller, \
	companylogincontroller, jobpostcontroller, companydashboardcontroller

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
			if validation.isValid:
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
			if validation.isValid:
				return redirect('/company/dashboard/')
			messages.error(
				request, errormessage.INVALID_USERNAME_OR_PASSWORD_ERROR
			)
			return render(request, 'login.html', {const.LOGIN_FORM : validation.response})
		except:
			messages.error(request, errormessage.INTERNAL_SERVER_ERROR)
			return render(request, 'login.html', context)

# @rolePermission([UserRole.objects.get(roleName='Company')])
#@decorator.unauthenticated_user
@login_required(login_url="/company/login/")
@decorator.allowed_users(allowed_roles=['Company'])
def companyDashboard(request):
	form = JobPostForm()
	if request.method == 'GET':
		context = {
			"isLogged": True,
			"userRole": "Company",
			"jobPostForm": form
		}
		try:
			validation = companydashboardcontroller.getJobPost(request)
			if validation.isValid:
				context.update(validation.response)
				return render(request, 'company/companyDashboard.html', context)
			messages.error(request, "Failed to load job posts!")
			return render(request, 'company/companyDashboard.html', context)
		except:
			messages.error(request, errormessage.INTERNAL_SERVER_ERROR)
			return render(request, 'company/companyDashboard.html', context)

@login_required(login_url="/company/login/")
@decorator.allowed_users(allowed_roles=['Company'])
def jobPostCreate(request):
	if request.method == 'POST':
		form = JobPostForm()
		context = {
			"jobPostForm": form,
			"userRole": "Company"
		}
		try:
			validation = jobpostcontroller.saveJobPost(request)
			print(validation.isValid)
			if validation.isValid:
				context.update(validation.response)
				print("DONE")
				return render(request, 'company/companyDashboard.html', context)
			messages.error(request, 'Job Post isnot Created!')
			return render(request, 'company/companyDashboard.html', context)
		except:
			messages.error(request, errormessage.INTERNAL_SERVER_ERROR)
			return render(request, 'company/companyDashboard.html', context)

@login_required(login_url="/company/login/")
@decorator.allowed_users(allowed_roles=['Company'])
def companyLogout(request):
	logout(request)
	return redirect('/home')
