from library.validationresponse import ValidationResponse
from apps.candidate.models import Candidate
from apps.resume.models import Resume, OtherSkills, ResumeAndOtherSkills, \
    Technology, ResumeAndTechnology, AcademicRecord, ResumeAndAcademicRecord

def getResume(request):
    candidate = Candidate.objects.get(user=request.user)
    resume = Resume.objects.filter(candidate=candidate).first()
    resumeAndOtherSkills = ResumeAndOtherSkills.objects.filter(resume=resume).all()
    resumeAndTechnology = ResumeAndTechnology.objects.filter(resume=resume).all()
    resumeAndAcademicRecord = ResumeAndAcademicRecord.objects.filter(resume=resume).all()
    response = {
        'candidate': candidate,
        'resume': resume,
        'allOtherSkills': resumeAndOtherSkills,
        'allTechnology': resumeAndTechnology,
        'allAcademicRecord': resumeAndAcademicRecord
    }
    return ValidationResponse(True, response, False)