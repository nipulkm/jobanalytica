from django.shortcuts import render, redirect
from apps.candidate.forms import CandidateRegistrationForm, CandidateLoginForm
from django.contrib import messages
from library import constants as const
from library import errormessage
from apps.candidate.controller import candidateregistrationcontroller, candidatelogincontroller

def home(request):
	return render(request, 'basetemplate.html')

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
	form = CandidateLoginForm()
	context = {const.CANDIDATE_LOGIN_FORM: form}
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
				return render(request, 'basetemplate.html')
			return render(request, 'login.html', validation.response)
		except:
			messages.error(request, errormessage.INTERNAL_SERVER_ERROR)
			return render(request, 'login.html', context)
