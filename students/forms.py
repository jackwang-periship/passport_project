
from django import forms
from .models import Student
from phonenumber_field.modelfields import PhoneNumberField


class StudentForm(forms.ModelForm):
    first_name = forms.CharField(label="first_name")
    last_name = forms.CharField(label="last_name")
    ssn = forms.IntegerField(label="ssn")
    zipcode = forms.CharField(label="zipcode")
    address = forms.CharField(label='address')
    country = forms.CharField(label="country")
    city = forms.CharField(label="city")
    cellPhone = PhoneNumberField()
    email = forms.EmailField(label="email")
    location = forms.CharField(label="location", required=False)
    refer = forms.CharField(label="refer", required=False)
    sources = forms.CharField(label="sources", required=False)
    gender = forms.CharField()

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

class ModifyStudentForm(forms.Form):
    RecId = forms.IntegerField()

