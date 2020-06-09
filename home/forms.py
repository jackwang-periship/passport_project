from django.contrib.auth.models import User
from django import forms
from .models import UserProfile, Employee
from .models import USER_TYPE_CHOICES, AVTECH_DEPARTMENT_CHOICES, AVTECH_EMPLOYEE_ROLE_CHOICES


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    type = forms.CharField(max_length=32, widget=forms.Select(choices=USER_TYPE_CHOICES))

    class Meta:
        model = UserProfile
        fields = ('website', 'picture')


class EmployeeForm(forms.ModelForm):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email = forms.EmailField(label='EMail')
    department = forms.ChoiceField(choices=AVTECH_DEPARTMENT_CHOICES)
    role = forms.ChoiceField(choices=AVTECH_EMPLOYEE_ROLE_CHOICES)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Employee
        fields = ('first_name', 'last_name', 'email', 'department', 'role')
