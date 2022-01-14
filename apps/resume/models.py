import uuid
from django.db import models
from library import constants as const
from apps.candidate.models import Candidate

class Resume(models.Model):
	resumeId = \
		models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
	phone = models.CharField(max_length=const.PHONE_NUMBER_MAX_LENGTH)
	email = models.EmailField(max_length = 254)
	candidate = models.ForeignKey(Candidate, on_delete=models.PROTECT)
	
	def __str__(self):
		return str(self.id) + " - " + str(self.candidate)

class OtherSkills(models.Model):
	description = models.CharField(max_length=const.DESCRIPTION_MAX_LENGTH)
	experience = models.IntegerField()

	def __str__(self):
		return str(self.description)

class ResumeAndOtherSkills(models.Model):
	resume = models.ForeignKey(Resume, on_delete=models.PROTECT)
	otherSkills = models.ForeignKey(OtherSkills, on_delete=models.PROTECT)

	def __str__(self):
		return str(self.resume)

class Technology(models.Model):
	technologyCode = models.CharField(max_length=const.TECHNOLOGY_CODE_MAX_LENGTH)
	technologyName = models.CharField(max_length=const.TECHNOLOGY_NAME_MAX_LENGTH)

	def __str__(self):
		return str(self.technologyName)

class ResumeAndTechnology(models.Model):
	resume = models.ForeignKey(Resume, on_delete=models.PROTECT)
	technology = models.ForeignKey(Technology, on_delete=models.PROTECT)
	experience = models.IntegerField()

	def __str__(self):
		return str(self.resume)

class AcademicRecord(models.Model):
	academyType = models.CharField(max_length=const.ACADEMY_TYPE_MAX_LENGTH)
	subject = models.CharField(max_length=const.SUBJECT_MAX_LENGTH)
	instituteName = models.CharField(max_length=const.INSTITUTE_NAME_MAX_LENGTH)
	passingYear = models.CharField(max_length=const.PASSING_YEAR_MAX_LENGTH)
	result = models.DecimalField(max_digits=const.DECIMAL_MAX_DIGIT, decimal_places=const.DECIMAL_PLACES_MAX_DIGIT)

	def __str__(self):
		return str(self.academyType)

class ResumeAndAcademicRecord(models.Model):
	resume =  models.ForeignKey(Resume, on_delete=models.PROTECT)
	academicRecord =  models.ForeignKey(AcademicRecord, on_delete=models.PROTECT)

	def __str__(self):
		return str(self.resume)
