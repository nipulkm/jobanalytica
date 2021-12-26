from library.validationresponse import ValidationResponse
from apps.company.models import Company, JobPost

def getJobPost(request):
	company = Company.objects.get(user=request.user)
	jobPosts = list(JobPost.objects.all().filter(company=company))
	response = {
		"jobPosts": jobPosts
	}
	return ValidationResponse(True, response, None)
