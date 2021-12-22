from django.contrib import admin
from apps.candidate.models import UserRole, Candidate

class UserRoleAdmin(admin.ModelAdmin):
	list_display = ['roleName', 'roleCode']

class CandidateAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'profileId',
		'name',
		'birthdate',
		'phone',
		'address',
		'user',
		'userRole'
	]

admin.site.register(UserRole, UserRoleAdmin)
admin.site.register(Candidate, CandidateAdmin)
