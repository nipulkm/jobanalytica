from django.contrib import admin
from apps.company.models import Company

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

admin.site.register(Company, CompanyAdmin)
