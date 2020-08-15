from django.contrib.auth.models import User
from django import forms
from .models import UserProfile
from .models import USER_ROLE_CHOICES, AVTECH_DEPARTMENT_CHOICES
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    role = forms.CharField(max_length=32, widget=forms.Select(choices=USER_ROLE_CHOICES))
    avtech_department = forms.CharField(max_length=32, widget=forms.Select(choices=AVTECH_DEPARTMENT_CHOICES))

    class Meta:
        model = UserProfile
        fields = ('website', 'picture', 'role', 'avtech_department')


class StudentSignupForm(SignupForm):
    def save(self, request):
        user = super(StudentSignupForm, self).save(request)
        student = Group.objects.get(name='Student')
        user.groups.add(student)
        return user
