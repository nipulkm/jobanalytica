from django import forms
from library import constants as const

class CompanyRegistrationForm(forms.Form):
	name = forms.CharField(max_length=const.COMPANY_NAME_MAX_LENGTH)
	type = forms.ChoiceField(choices=([('software company','Software Company')]))
	employee = forms.IntegerField(required=False)
	address = forms.CharField(required=False)
	phone = forms.CharField(max_length=const.PHONE_NUMBER_MAX_LENGTH)
	username = forms.EmailField()
	password = forms.CharField(
		max_length=const.PASSWORD_MAX_LENGTH,
		min_length=const.PASSWORD_MIN_LENGTH,
		widget=forms.PasswordInput
	)

class JobPostForm(forms.Form):
	position = forms.CharField(max_length=const.POSITION_MAX_LENGTH)
	description = forms.CharField(widget=forms.Textarea)
	experience = forms.IntegerField(required=False)
	salary = forms.IntegerField(required=False)
	deadline = forms.DateField(required=False)
	# description.widget.attrs.update({
	# 	'id': 'description'
	# })
