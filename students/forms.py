from django import forms
from .models import Student
from phonenumber_field.formfields import PhoneNumberField
from django.core import validators
import students.widgets as widgets


def validate_ssn(value):
    cleaned = value.replace('-', '')
    if len(cleaned) != 9 or not cleaned.isdigit():
        raise forms.ValidationError('Please enter a valid SSN.')

def validate_zip_code(value):
    if len(value) != 5 or not value.isdigit():
        raise forms.ValidationError('Please enter a valid ZIP code.')

class StudentForm(forms.ModelForm):
    # first_name = forms.CharField(max_length=20)
    # last_name = forms.CharField(max_length=20)
    ssn = forms.CharField(max_length=11, validators=[validate_ssn],  widget=widgets.forms.TextInput(attrs={'data-mask':"000-00-0000"}))
    zipcode = forms.CharField(max_length=10, validators=[validate_zip_code])
    # homeAddress = forms.CharField()
    # country = forms.CharField(max_length=50)
    # city = forms.CharField(max_length=30)
    # cellPhone = PhoneNumberField()
    # email = forms.EmailField()
    # location = forms.CharField(max_length=30)
    # refer = forms.CharField(max_length=30)
    # sources = forms.CharField(max_length=30)
    # gender = forms.CharField(max_length=10)

    class Meta:
        model = Student
        fields = (
            'first_name', 'last_name', 'ssn', 'homeAddress', 'zipcode', 'cellPhone', 'email',
            'location',
            'refer', 'sources', 'gender')

    def clean_ssn(self):
        ssn = self.cleaned_data.get('ssn')
        return ssn.replace('-', '')


class SearchStudentForm(forms.Form):
    first_name = forms.CharField(max_length=20, required=False)
    last_name = forms.CharField(max_length=20, required=False)
    cellPhone = PhoneNumberField(required=False)
    email = forms.EmailField(required=False)
    ssn = forms.CharField(required=False)
    address = forms.CharField(required=False)
    zipcode = forms.CharField(required=False)

    def clean(self):
        if not self.has_changed():
            raise forms.ValidationError('At least one field must be filled out.')


class ModifyStudentInfoForm(forms.ModelForm):
    zipcode = forms.CharField(max_length=10, validators=[validate_zip_code])

    class Meta:
        model = Student
        fields = (
            'first_name', 'last_name', 'ssn', 'homeAddress', 'zipcode', 'country', 'city', 'cellPhone', 'email',
            'location',
            'refer', 'sources', 'gender')

    # def validate(self):
    #     email = self.cleaned_data.get('email')
    #     validate_email(email)

    # def validate_zip_code(self):
    #     zipcode = self.cleaned_data.get('zipcode')
    #     if len(zipcode) != 5 or not zipcode.isdigit():
    #         raise forms.ValidationError('Please enter a valid ZIP code.')
    #
    # def validate_ssn(value):
    #     cleaned = value.replace('-', '')
    #     if len(cleaned) != 9 or not cleaned.isdigit():
    #         raise forms.ValidationError('Please enter a valid SSN.')