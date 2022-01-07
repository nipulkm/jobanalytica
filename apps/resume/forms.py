from django import forms

class ResumeForm(forms.Form):
	phone = forms.CharField(required=False)
	email = forms.EmailField()
	technology1 = forms.ChoiceField(choices=([('', 'Select One'), ('c', 'C'), ('c++', 'C++'), ('python', 'Python')]), required=False)
	experience1 = forms.IntegerField(required=False)
	technology2 = forms.ChoiceField(choices=([('', 'Select One'), ('c', 'C'), ('c++', 'C++'), ('python', 'Python')]), required=False)
	experience2 = forms.IntegerField(required=False)
	technology3 = forms.ChoiceField(choices=([('', 'Select One'), ('c', 'C'), ('c++', 'C++'), ('python', 'Python')]), required=False)
	experience3 = forms.IntegerField(required=False)
	academyType1 = forms.ChoiceField(choices=([('', 'Select One'), ('diploma','Diploma'), ('hsc','H.S.C'), ('bsc','B.Sc')]), required=False)
	subject1 = forms.CharField(required=False)
	instituteName1 = forms.CharField(required=False)
	passingYear1 = forms.CharField(required=False)
	result1 = forms.DecimalField(required=False)
	academyType2 = forms.ChoiceField(choices=([('', 'Select One'), ('diploma','Diploma'), ('hsc','H.S.C'), ('bsc','B.Sc')]), required=False)
	subject2 = forms.CharField(required=False)
	instituteName2 = forms.CharField(required=False)
	passingYear2 = forms.CharField(required=False)
	result2 = forms.DecimalField(required=False)
	skillDescription1 = forms.CharField(required=False)
	skillExperience1 = forms.IntegerField(required=False)
	skillDescription2 = forms.CharField(required=False)
	skillExperience2 = forms.IntegerField(required=False)