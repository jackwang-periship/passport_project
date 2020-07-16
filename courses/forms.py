from django.contrib.auth.models import User
from django import forms
from .models import UserProfile, Course
from .models import LOCATION_CHOICES, SUBJECT_CHOICES
from home.models import USER_ROLE_CHOICES

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class SubjectForm(forms.ModelForm):
    type = forms.CharField(max_length=32, widget=forms.Select(choices=USER_ROLE_CHOICES))

    class Meta:
        model = UserProfile
        fields = ('website', 'picture')


class CourseForm(forms.ModelForm):
    name = forms.CharField(max_length=70, label="Course Name", widget=forms.TextInput(attrs={'size':'36', 'placeholder': 'Course name'}))
    slug = forms.EmailField(label='EMail')
    subject = forms.CharField(max_length=32, widget=forms.Select(choices=SUBJECT_CHOICES, attrs={'style': 'width:256px'}))
    description = forms.TextInput()
    location = forms.CharField(max_length=32, widget=forms.Select(choices=LOCATION_CHOICES, attrs={'style': 'width:256px'}))

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Course
        fields = ('name', 'description', 'location')

    def save(self, Course=None):
        my_course = super(CourseForm, self).save(commit=False)
        my_course.save()
        return my_course