import uuid
from django.db import models
from django.contrib.auth.models import User
from library import constants as const
from apps.candidate.models import UserRole

class Company(models.Model):
	id = models.BigAutoField(primary_key=True)
	profileId = \
		models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
	name = models.CharField(max_length=const.COMPANY_NAME_MAX_LENGTH)
	type = models.CharField(
		max_length=const.COMPANY_TYPE_MAX_LENGTH
	)
	employee = models.IntegerField(
		blank=True, null=True
	)
	address = models.CharField(
		max_length=const.ADDRESS_MAX_LENGTH, blank=True, null=True
	)
	phone = models.CharField(max_length=const.PHONE_NUMBER_MAX_LENGTH)
	user = models.OneToOneField(User, on_delete=models.PROTECT)
	userRole = models.ForeignKey(UserRole, on_delete=models.PROTECT)

	def __str__(self):
		return str(self.id) + " - " + str(self.name)
