
from django import forms
from .models import Student
from phonenumber_field.modelfields import PhoneNumberField


class StudentForm(forms.ModelForm):
    YES = 'Yes'
    NO = 'No'
    MALE = 'Male'
    FEMALE = 'Female'
    GENDER = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    Chooses = (
        (YES, 'Yes'),
        (NO, 'No'),
    )
    first_name = forms.CharField(label="first_name")
    last_name = forms.CharField(label="last_name")
    ssn = forms.IntegerField(label="ssn")
    zipcode = forms.CharField(label="zipcode")
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
            'first_name', 'last_name', 'ssn', 'zipcode', 'country', 'city', 'cellPhone', 'email',
            'location',
            'refer', 'sources', 'gender')


class SearchStudentForm(forms.Form):
    first_name = forms.CharField(max_length=20, required=False)
    last_name = forms.CharField(max_length=20, required=False)
    ID = forms.IntegerField(required=False)

class ModifyStudentForm(forms.Form):
    ID = forms.IntegerField()

class ChangePasswordForm(forms.Form):
    OldPassword = forms.IntegerField()
    NewPassword = forms.IntegerField()
    ConfirmPassword = forms.IntegerField()

    class Meta:
        fields = (
            'old_password', 'new_password', 'confirm password'
        )
