import uuid
from django.db import models
from django.contrib.auth.models import User
from library import constants as const
from apps.candidate.models import UserRole, Candidate

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

class JobPost(models.Model):
	id = models.BigAutoField(primary_key=True)
	jobId = \
		models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
	company = models.ForeignKey(Company, on_delete=models.PROTECT)
	technology = models.CharField(max_length=30)
	position = models.CharField(max_length=const.POSITION_MAX_LENGTH)
	experience = models.IntegerField(blank=True, null=True)
	salary = models.IntegerField(blank=True, null=True)
	description = models.TextField()
	deadline = models.DateField(blank=True, null=True)
	appliedNumber = models.IntegerField(default=0)
	isDeleted = models.BooleanField(default=False)

	def __str__(self):
		return str(self.id) + " - " + str(self.position)

class CandidateJobPost(models.Model):
	candidate = models.ForeignKey(Candidate, on_delete=models.PROTECT)
	jobPost = models.ForeignKey(JobPost, on_delete=models.PROTECT)