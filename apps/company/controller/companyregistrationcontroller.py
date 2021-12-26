from django.contrib.auth.models import User, Group
from apps.company.forms import CompanyRegistrationForm
from library.validationresponse import ValidationResponse
from apps.candidate.models import UserRole
from apps.company.models import Company

def createRegistration(formData):
	username=formData['username']
	password=formData['password']
	group = Group.objects.get(name='Company')
	user = User.objects.create_user(username=username, password=password)
	user.groups.add(group)
	userRole = UserRole.objects.get(roleName='Company')
	company = Company(
		name=formData['name'],
		type=formData['type'],
		employee=formData['employee'],
		address=formData['address'],
		phone=formData['phone'],
		user=user,
		userRole=userRole
	)
	company.save()
	return ValidationResponse(True, True, None)

def companyRegistrationFormValidation(request):
	form = CompanyRegistrationForm(request.POST)
	if not form.is_valid():
		response = {const.COMPANY_REGISTRATION_FORM: form}
		return ValidationResponse(False, response, None)
	return createRegistration(form.cleaned_data)
