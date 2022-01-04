from library.validationresponse import ValidationResponse
from apps.candidate.models import Candidate
from apps.resume.models import Resume, OtherSkills, ResumeAndOtherSkills, \
    Technology, ResumeAndTechnology, AcademicRecord, ResumeAndAcademicRecord
from apps.resume.forms import ResumeForm

def saveResume(request):
    form = ResumeForm(request.POST)
    response = { "resumeForm": form}
    if form.is_valid():
        formData = form.cleaned_data
        candidate = Candidate.objects.get(user=request.user)
        resume = Resume(
            phone=formData['phone'],
            email=formData['email'],
            candidate=candidate
        )
        resume.save()
        response.update({'resume': resume})
        if formData['technology1']:
            technology1 = Technology(
                technology=formData['technology1'],
                experience=formData['experience1']
            )
            technology1.save()
            resumeAndTechnology1 = ResumeAndTechnology(
                resume=resume,
                technology=technology1
            )
            resumeAndTechnology1.save()
            response.update({'technology1': technology1, 'resumeAndTechnology1': resumeAndTechnology1})
        if formData['technology2']:
            technology2 = Technology(
                technology=formData['technology2'],
                experience=formData['experience2']
            )
            technology2.save()
            resumeAndTechnology2 = ResumeAndTechnology(
                resume=resume,
                technology=technology2
            )
            resumeAndTechnology2.save()
            response.update({'technology2': technology2, 'resumeAndTechnology2': resumeAndTechnology2})
        if formData['technology3']:
            technology3 = Technology(
                technology=formData['technology3'],
                experience=formData['experience3']
            )
            technology3.save()
            resumeAndTechnology3 = ResumeAndTechnology(
                resume=resume,
                technology=technology3
            )
            resumeAndTechnology3.save()
            response.update({'technology3': technology3, 'resumeAndTechnology3': resumeAndTechnology3})
        if formData['academyType1']:
            academicRecord1 = AcademicRecord(
                academyType=formData['academyType1'],
                subject=formData['subject1'],
                instituteName=formData['instituteName1'],
                passingYear=formData['passingYear1'],
                result=formData['result1']
            )
            academicRecord1.save()
            resumeAndAcademicRecord1 = ResumeAndAcademicRecord(
                resume=resume,
                academicRecord=academicRecord1
            )
            resumeAndAcademicRecord1.save()
            response.update({'academicRecord1': academicRecord1, 'resumeAndAcademicRecord1': resumeAndAcademicRecord1})
        if formData['academyType2']:
            academicRecord2 = AcademicRecord(
                academyType=formData['academyType2'],
                subject=formData['subject2'],
                instituteName=formData['instituteName2'],
                passingYear=formData['passingYear2'],
                result=formData['result2']
            )
            academicRecord2.save()
            resumeAndAcademicRecord2 = ResumeAndAcademicRecord(
                resume=resume,
                academicRecord=academicRecord2
            )
            academicRecord2.save()
            response.update({'academicRecord2': academicRecord2, 'resumeAndAcademicRecord2': resumeAndAcademicRecord2})
        if formData['skillDescription1']:
            otherSkills1 = OtherSkills(
                description=formData['skillDescription1'],
                experience=formData['skillExperience1']
            )
            otherSkills1.save()
            resumeAndOtherSkills1 = ResumeAndOtherSkills(
                resume=resume,
                otherSkills=otherSkills1
            )
            resumeAndOtherSkills1.save()
            response.update({'otherSkills1': otherSkills1, 'resumeAndOtherSkills1': resumeAndOtherSkills1})
        if formData['skillDescription2']:
            otherSkills2 = OtherSkills(
                description=formData['skillDescription2'],
                experience=formData['skillExperience2']
            )
            otherSkills2.save()
            resumeAndOtherSkills2 = ResumeAndOtherSkills(
                resume=resume,
                otherSkills=otherSkills2
            )
            resumeAndOtherSkills1.save()
            response.update({'otherSkills2': otherSkills2, 'resumeAndOtherSkills2': resumeAndOtherSkills2})
        return ValidationResponse(True, response, False)
    return ValidationResponse(False, response, False)