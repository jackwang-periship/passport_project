
from django import forms
from .models import Student
from phonenumber_field.modelfields import PhoneNumberField


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = (
            'first_name', 'last_name', 'ssn', 'zipcode', 'address', 'country', 'city', 'cellPhone', 'email',
            'location',
            'refer', 'sources', 'gender')


class SearchStudentForm(forms.Form):
    first_name = forms.CharField(max_length=20, required=False)
    last_name = forms.CharField(max_length=20, required=False)
    cellPhone = forms.IntegerField(required=False)
    email = forms.CharField(required=False)

class ModifyStudentForm(forms.Form):
    RecId = forms.IntegerField()

