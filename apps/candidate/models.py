import uuid
from django.db import models
from django.contrib.auth.models import User
from library import constants as const

class UserRole(models.Model):
	roleName = models.CharField(max_length=const.USER_ROLE_NAME_MAX_LENGTH)
	roleCode = models.CharField(max_length=const.USER_ROLE_CODE_MAX_LENGTH)

	def __str__(self):
		return str(self.roleName)

class Candidate(models.Model):
	id = models.BigAutoField(primary_key=True)
	profileId = \
		models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
	name = models.CharField(max_length=const.COMPANY_NAME_MAX_LENGTH)
	birthdate = models.DateField()
	phone = models.CharField(max_length=const.PHONE_NUMBER_MAX_LENGTH)
	address = models.CharField(
		max_length=const.ADDRESS_MAX_LENGTH, blank=True, null=True
	)
	user = models.OneToOneField(User, on_delete=models.PROTECT)
	userRole = models.ForeignKey(UserRole, on_delete=models.PROTECT)

	def __str__(self):
		return str(self.id) + " - " + str(self.name)

