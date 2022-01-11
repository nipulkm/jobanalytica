from library.validationresponse import ValidationResponse
from apps.company.models import JobPost

def getDashboardData(request):
    print("OKAY44444444")
    totalJobPost = JobPost.objects.count()
    dotNet = JobPost.objects.filter(technology='C# Dot Net').count()
    laravel = JobPost.objects.filter(technology='PHP Laravel').count()
    django = JobPost.objects.filter(technology='Python Django').count()
    dotNet = int((dotNet*100)/totalJobPost)
    laravel = int((laravel*100)/totalJobPost)
    django = int((django*100)/totalJobPost)
    others = 100 - (dotNet+laravel+django)
    print("OKAY")
    response = {
        'dotNet': 'C# Dot Net','dotNetPercentage': dotNet,
        'laravel': 'PHP Laravel','laravelPercentage': laravel,
        'django': 'Python Django','djangoPercentage': django,
        'others': 'Others', 'othersPercentage': others
    }
    return ValidationResponse(True, response, None)