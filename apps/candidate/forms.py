from django import forms
from library import constants as const

class CandidateRegistrationForm(forms.Form):
	name = forms.CharField(max_length=const.CANDIDATE_NAME_MAX_LENGTH)
	birthdate = forms.DateField()
	phone = forms.CharField(max_length=const.PHONE_NUMBER_MAX_LENGTH)
	address = forms.CharField(required=False)
	username = forms.EmailField()
	password = forms.CharField(
		max_length=const.PASSWORD_MAX_LENGTH,
		min_length=const.PASSWORD_MIN_LENGTH,
		widget=forms.PasswordInput
	)

	birthdate.widget.attrs.update({'class': 'fas fa-calendar input-prefix', 'type': 'date'})

class LoginForm(forms.Form):
	username = forms.EmailField(max_length=const.USERNAME_MAX_LENGTH)
	password = forms.CharField(
		max_length=const.PASSWORD_MAX_LENGTH,
		min_length=const.PASSWORD_MIN_LENGTH,
		widget=forms.PasswordInput
	)
