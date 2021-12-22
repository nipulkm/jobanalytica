from django.shortcuts import render, redirect
from apps.candidate.forms import CandidateRegistrationForm, CandidateLoginForm
from django.contrib import messages
from library import constants as const
from library import errormessage
from apps.candidate.controller import candidateregistrationcontroller

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
		except:
			messages.error(request, errormessage.INTERNAL_SERVER_ERROR)
			return render(request, 'candidate/candidateRegistration.html')
def candidateLogin(request):
	if request.method == 'GET':
		form = CandidateLoginForm()
		context = {const.CANDIDATE_LOGIN_FORM: form}
		try:
			return render(request, 'login.html', context)
		except:
			messages.error(request, errormessage.INTERNAL_SERVER_ERROR)
			return render(request, 'login.html', context)
	if request.method == 'POST':
		try:
			validation = candidateregistrationcontroller.candidateRegistrationFormValidation(request)
			if validation.isValid == True:
				return redirect('/candidate/login/')
		except:
			messages.error(request, errormessage.INTERNAL_SERVER_ERROR)
			return render(request, 'candidate/candidateRegistration.html')
