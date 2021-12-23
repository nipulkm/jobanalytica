from django.contrib.auth.models import User
from apps.candidate.forms import CandidateRegistrationForm
from library.validationresponse import ValidationResponse
from apps.candidate.models import UserRole, Candidate

def createRegistration(formData):
	username=formData['username']
	password=formData['password']
	user = User.objects.create_user(username=username, password=password)
	userRole = UserRole.objects.get(roleName='Candidate')
	candidate = Candidate(
		name=formData['name'],
		birthdate=formData['birthdate'],
		phone=formData['phone'],
		address=formData['address'],
		user=user,
		userRole=userRole
	)
	candidate.save()
	return ValidationResponse(True, True, None)

def candidateRegistrationFormValidation(request):
	form = CandidateRegistrationForm(request.POST)
	if not form.is_valid():
		response = {const.CANDIDATE_REGISTRATION_FORM: form}
		return ValidationResponse(False, response, None)
	return createRegistration(form.cleaned_data)
