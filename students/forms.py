from django.contrib.auth.models import User
from django import forms
from .models import Student


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
    first_name = forms.CharField(max_length=30, label="first_name")
    last_name = forms.CharField(max_length=30, label="last_name")
    ssn = forms.IntegerField(max_length=9, label="ssn")
    zipcode = forms.CharField(max_length=5, label="zipcode")
    country = forms.CharField(max_length=50, default="United States of America", label="country")
    city = forms.CharField(max_length=30, label="city")
    cellPhone = forms.IntegerField(max_length=15, label="cellPhone")
    homePhone = forms.IntegerField(max_length=15, label="homePhone")
    email = forms.CharField(max_length=30, label="email")
    location = forms.CharField(max_length=30, label="location")
    refer = forms.CharField(max_length=30, default="No Refer", label="refer")
    sources = forms.CharField(max_length=30, default="Individual", label="sources")
    notes = forms.TextInput()
    gender = forms.CharField(max_length=10, choices=GENDER, default=MALE)
    newsLetter = forms.CharField(max_length=3, choices=Chooses, default=YES)

    class Meta:
        model = Student
        fields = (
            'first_name', 'last_name', 'ssn', 'zipcode', 'country', 'city', 'cellPhone', 'homePhone', 'email',
            'location',
            'refer', 'sources', 'notes', 'gender', 'newsLetter')