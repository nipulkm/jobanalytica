from library.validationresponse import ValidationResponse
from apps.candidate.models import Candidate
from apps.resume.models import Resume, OtherSkills, ResumeAndOtherSkills, \
    Technology, ResumeAndTechnology, AcademicRecord, ResumeAndAcademicRecord

def getResume(request):
    candidate = Candidate.objects.get(user=request.user)
    print(candidate)
    resume = Resume.objects.filter(candidate=candidate).first()
    print(resume)
    resumeAndOtherSkills = ResumeAndOtherSkills.objects.filter(resume=resume).all()
    print(resumeAndOtherSkills)
    resumeAndTechnology = ResumeAndTechnology.objects.filter(resume=resume).all()
    print(resumeAndTechnology)
    resumeAndAcademicRecord = ResumeAndAcademicRecord.objects.filter(resume=resume).all()
    response = {
        'candidate': candidate,
        'resume': resume,
        'allOtherSkills': resumeAndOtherSkills,
        'allTechnology': resumeAndTechnology,
        'allAcademicRecord': resumeAndAcademicRecord
    }
    print(response)
    return ValidationResponse(True, response, False)