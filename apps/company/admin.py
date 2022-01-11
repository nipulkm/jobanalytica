from django.contrib import admin
from apps.company.models import Company, JobPost, CandidateJobPost

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
		'technology',
		'position',
		'experience',
		'salary',
		'description',
		'deadline',
		'appliedNumber',
		'isDeleted'
	]

class CandidateJobPostAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'candidate',
		'jobPost'
	]
admin.site.register(Company, CompanyAdmin)
admin.site.register(JobPost, JobPostAdmin)
admin.site.register(CandidateJobPost, CandidateJobPostAdmin)