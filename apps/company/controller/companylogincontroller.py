from django.contrib.auth import authenticate, login
from library.validationresponse import ValidationResponse
from library import constants as const
from apps.company.validation import formvalidation

def authentication(request, form):
	username = form.cleaned_data[const.USERNAME_PROPERTY]
	password = form.cleaned_data[const.PASSWORD_PROPERTY]
	user = authenticate(request, username=username, password=password)
	if user:
		return ValidationResponse(True, user, None)
	return ValidationResponse(False, form, None)

def loginFormValidation(request):
	form = formvalidation.getLoginForm(request)
	if not form.isValid:
		return ValidationResponse(False, form.response, None)
	user = authentication(request, form.response)
	if user.isValid:
		login(request, user.response)
		return ValidationResponse(True, None, None)
	return ValidationResponse(False, form.response, None)
