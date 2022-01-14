from library.validationresponse import ValidationResponse
from apps.company.models import JobPost

def getJobPost(request):
    jobPosts = list(JobPost.objects.all())
    response = {
        'jobPosts': jobPosts
    }
    return ValidationResponse(True, response, False)