from library.validationresponse import ValidationResponse
from apps.company.models import JobPost, CandidateJobPost
from apps.candidate.models import Candidate

def apply(request, jobId):
    candidate = Candidate.objects.get(user=request.user)
    
    jobPost = JobPost.objects.get(jobId=jobId)
    candidateJobPost = CandidateJobPost(
        candidate=candidate,
        jobPost=jobPost
    )
    candidateJobPost.save()
    
    appliedNumber = jobPost.appliedNumber + 1
    print("KKKKKKKK", jobPost)
    JobPost.objects.filter(jobId=jobId).update(appliedNumber=appliedNumber)
    print("OKAYYYYYYYY: ", jobPost.appliedNumber)
    return ValidationResponse(True, True, None)