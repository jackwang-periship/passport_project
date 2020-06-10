from django.contrib.auth.models import User
from django import forms
from .models import UserProfile, Course
from .models import LOCATION_CHOICES
from home.models import AVTECH_DEPARTMENT_CHOICES, USER_TYPE_CHOICES

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class SubjectForm(forms.ModelForm):
    type = forms.CharField(max_length=32, widget=forms.Select(choices=USER_TYPE_CHOICES))

    class Meta:
        model = UserProfile
        fields = ('website', 'picture')


class CourseForm(forms.ModelForm):
    name = forms.CharField(max_length=70, label="Course Name", widget=forms.TextInput(attrs={'size':'36', 'placeholder': 'Course name'}))
    slug = forms.EmailField(label='EMail')
    department = forms.ChoiceField(choices=AVTECH_DEPARTMENT_CHOICES)
    description = forms.TextInput()
    location = forms.CharField(max_length=32, widget=forms.Select(choices=LOCATION_CHOICES, attrs={'style': 'width:256px'}))

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Course
        fields = ('name', 'department', 'department')
