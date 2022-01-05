from library.validationresponse import ValidationResponse
from apps.company.models import JobPost

def getjobpost(request):
    jobPosts = list(JobPost.objects.all())
    response = {
        'jobPosts': jobPosts
    }
    return ValidationResponse(True, response, False)