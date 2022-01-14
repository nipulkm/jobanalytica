from library.validationresponse import ValidationResponse
from apps.company.forms import JobPostForm
from apps.company.models import JobPost, Company

def saveJobPost(request):
	company = Company.objects.get(user=request.user)
	form = JobPostForm(request.POST)
	if form.is_valid():
		formData = form.cleaned_data
		jobPost = JobPost (
			company=company,
			technology=formData['technology'],
			position=formData['position'],
			experience=formData['experience'],
			salary=formData['salary'],
			description=formData['description'],
			deadline=formData['deadline']
		)
		jobPost.save()
		jobPosts = list(JobPost.objects.all().filter(company=company))
		response = {
			"jobPosts": jobPosts
		}
		return ValidationResponse(True, response, None)
	return ValidationResponse(False, form.response, None)
