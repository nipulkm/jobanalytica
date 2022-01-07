from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from library import constants as const, decorator
from library import errormessage
from apps.candidate.models import Candidate
from apps.resume.models import Resume
from apps.resume.controller import viewresume
from apps.candidate.forms import CandidateRegistrationForm, LoginForm
from apps.candidate.controller import candidateregistrationcontroller, candidatelogincontroller, \
	jobpostcontroller

def home(request):
	if request.method == 'GET':
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name
			context = {"isLogged": True, "userRole": group}
		else:
			context = {"isLogged": False, "userRole": None}
		try:
			validation = jobpostcontroller.getJobPost(request)
			if validation.isValid:
				context.update(validation.response)
				return render(request, 'candidate/candidatehomepage.html', context)
			messages.error(request, 'Failed to fecth job post from DB!')
			return render(request, 'login.html', context)
		except:
			messages.error(request, errormessage.INTERNAL_SERVER_ERROR)
			return render(request, 'login.html', context)

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

@decorator.unauthenticated_user
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
			messages.error(
				request, errormessage.INVALID_USERNAME_OR_PASSWORD_ERROR
			)
			return render(request, 'login.html', {const.LOGIN_FORM_PROPERTY : validation.response})
		except:
			messages.error(request, errormessage.INTERNAL_SERVER_ERROR)
			return render(request, 'login.html', context)

@login_required(login_url="/candidate/login/")
@decorator.allowed_users(allowed_roles=['Candidate'])
def candidateDashboard(request):
	if request.method == 'GET':
		context = {
			"isLogged": True,
			"userRole": "Candidate"
		}
		return render(request, 'candidate/candidateDashboard.html', context)

@login_required(login_url="/candidate/login/")
@decorator.allowed_users(allowed_roles=['Candidate'])
def profile(request):
	if request.method == 'GET':
		context = {
			"isLogged": True,
			"userRole": "Candidate"
		}
		candidate = Candidate.objects.get(user=request.user)
		if Resume.objects.filter(candidate=candidate).first():
			try:
				validation = viewresume.getResume(request)
				if validation.isValid:
					context.update({'isResume': True})
					context.update(validation.response)
					return render(request, 'candidate/candidateprofile.html', context)
				messages.error(
					request, 'Failed to fetch DB!'
				)
				return redirect('/home')
			except:
				messages.error(request, errormessage.INTERNAL_SERVER_ERROR)
				return redirect('/home')
		else:
			candidate = list(Candidate.objects.get(candidate__user=request.user))
			context.update({'isResume': False, 'candidate': candidate})
			return render(request, 'candidate/profile.html', context)

@login_required(login_url="/candidate/login/")
@decorator.allowed_users(allowed_roles=['Candidate'])
def candidateLogout(request):
	logout(request)
	return redirect('/home')
