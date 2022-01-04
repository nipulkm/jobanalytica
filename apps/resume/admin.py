from django.contrib import admin
from apps.resume.models import Resume, OtherSkills, ResumeAndOtherSkills, \
	Technology, ResumeAndTechnology, AcademicRecord, ResumeAndAcademicRecord

class ResumeAdmin(admin.ModelAdmin):
	list_display = [
		'id', 'resumeId', 'candidate'
	]

class OtherSkillsAdmin(admin.ModelAdmin):
	list_display = [
		'description', 'experience'
	]

class ResumeAndOtherSkillsAdmin(admin.ModelAdmin):
	list_display = [
		'resume', 'otherSkills'
	]

class TechnologyAdmin(admin.ModelAdmin):
	list_display = [
		'technologyCode', 'technologyName'
	]

class ResumeAndTechnologyAdmin(admin.ModelAdmin):
	list_display = [
		'resume', 'technology', 'experience'
	]

class AcademicRecordAdmin(admin.ModelAdmin):
	list_display = [
		'academyType', 'subject', 'instituteName', 'passingYear', 'result'
	]

class ResumeAndAcademicRecordAdmin(admin.ModelAdmin):
	list_display = [
		'resume', 'academicRecord'
	]

admin.site.register(Resume, ResumeAdmin)
admin.site.register(OtherSkills, OtherSkillsAdmin)
admin.site.register(ResumeAndOtherSkills, ResumeAndOtherSkillsAdmin)
admin.site.register(Technology, TechnologyAdmin)
admin.site.register(ResumeAndTechnology, ResumeAndTechnologyAdmin)
admin.site.register(AcademicRecord, AcademicRecordAdmin)
admin.site.register(ResumeAndAcademicRecord, ResumeAndAcademicRecordAdmin)
