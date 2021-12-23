from library.validationresponse import ValidationResponse
from apps.candidate.forms import CandidateLoginForm

def getLoginForm(request):
	loginForm = CandidateLoginForm(request.POST)
	if not loginForm.is_valid():
		return ValidationResponse(False, loginForm, None)
	return ValidationResponse(True, loginForm, None)
