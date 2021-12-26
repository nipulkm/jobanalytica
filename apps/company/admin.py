from django.contrib import admin
from apps.company.models import Company, JobPost

class CompanyAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'profileId',
		'name',
		'type',
		'employee',
		'address',
		'phone',
		'user',
		'userRole'
	]

class JobPostAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'jobId',
		'company',
		'position',
		'experience',
		'salary',
		'description',
		'deadline',
		'appliedNumber',
		'isDeleted'
	]

admin.site.register(Company, CompanyAdmin)
admin.site.register(JobPost, JobPostAdmin)
