from library.validationresponse import ValidationResponse
from apps.candidate.forms import LoginForm

def getLoginForm(request):
	loginForm = LoginForm(request.POST)
	if not loginForm.is_valid():
		return ValidationResponse(False, loginForm, None)
	return ValidationResponse(True, loginForm, None)
