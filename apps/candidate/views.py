from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from library import constants as const
from library import errormessage
from apps.candidate.forms import CandidateRegistrationForm, LoginForm
from apps.candidate.controller import candidateregistrationcontroller, candidatelogincontroller

def home(request):
	context = {"isLogged": False}
	return render(request, 'basetemplate.html', context)

def candidateRegistration(request):
	if request.method == 'GET':
		form = CandidateRegistrationForm()
		context = {const.CANDIDATE_REGISTRATION_FORM: form}
		try:
			return render(request, 'candidate/candidateRegistration.html', context)
		except:
			messages.error(request, errormessage.INTERNAL_SERVER_ERROR)
			return render(request, 'candidate/candidateRegistration.html', context)
	if request.method == 'POST':
		try:
			validation = candidateregistrationcontroller.candidateRegistrationFormValidation(request)
			if validation.isValid == True:
				return redirect('/candidate/login/')
			return render(request, 'candidate/candidateRegistration.html', validation.response)
		except:
			form = CandidateRegistrationForm(request.POST)
			context = {const.CANDIDATE_REGISTRATION_FORM: form}
			messages.error(request, errormessage.INTERNAL_SERVER_ERROR)
			return render(request, 'candidate/candidateRegistration.html', context)
def candidateLogin(request):
	form = LoginForm()
	context = {
		const.LOGIN_FORM_PROPERTY: form,
		"userRole": "Candidate"
	}
	if request.method == 'GET':
		try:
			return render(request, 'login.html', context)
		except:
			messages.error(request, errormessage.INTERNAL_SERVER_ERROR)
			return render(request, 'login.html', context)
	if request.method == 'POST':
		try:
			validation = candidatelogincontroller.loginFormValidation(request)
			if validation.isValid == True:
				context.update({"isLogged": True})
				return render(request, 'basetemplate.html', context)
			return render(request, 'login.html', validation.response)
		except:
			messages.error(request, errormessage.INTERNAL_SERVER_ERROR)
			return render(request, 'login.html', context)

def candidateLogout(request):
	logout(request)
	return redirect('/home')
