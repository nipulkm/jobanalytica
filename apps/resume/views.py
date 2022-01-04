from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from library import errormessage
from library import constants as const, decorator
from apps.resume.forms import ResumeForm
from apps.resume.controller import createresume, viewresume

@login_required(login_url="/candidate/login/")
@decorator.allowed_users(allowed_roles=['Candidate'])
def createResume(request):
	if request.method == 'GET':
		resumeForm = ResumeForm()
		context = {
			'resumeForm': resumeForm
		}
		try:
			return render(request, 'resume/createresume.html', context)
		except:
			messages.error(request, errormessage.INTERNAL_SERVER_ERROR)
			return render(request, 'resume/createresume.html', context)
	if request.method == 'POST':
		form = ResumeForm(request.POST)
		context = {
			'resumeForm': form
		}
		try:
			validation = createresume.saveResume(request)
			if validation.isValid:
				return render(request, 'resume/viewresume.html', validation.response)
			messages.error(
				request, 'Invalid form data'
			)
			return render(request, 'resume/createresume.html', {'resumeForm' : validation.response})
		except:
			messages.error(request, errormessage.INTERNAL_SERVER_ERROR)
			return render(request, 'resume/createresume.html', context)

def viewResume(request):
	if request.method == 'GET':
		form = ResumeForm()
		context = {
			'resumeForm': form
		}
		try:
			validation = viewresume.getResume(request)
			if validation.isValid:
				return render(request, 'resume/viewresume.html', validation.response)
			messages.error(
				request, 'Failed to fetch DB!'
			)
			return render(request, 'resume/createresume.html', context)
		except:
			messages.error(request, errormessage.INTERNAL_SERVER_ERROR)
			return render(request, 'resume/createresume.html', context)