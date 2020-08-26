from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth import password_validation
from wiawdp.formfields import EmailField


class ChangePasswordForm(forms.Form):
    username = forms.CharField(required=True)
    new_password = forms.CharField(required=True, widget=forms.PasswordInput)
    confirm_new_password = forms.CharField(required=True, widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError('Username not recognized.', code='invalid')

        return username

    def clean_new_password(self):
        password = self.cleaned_data['new_password']
        password_validation.validate_password(password)
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_new_password')

        if password != confirm_password:
            raise forms.ValidationError('Passwords do not match.', code='invalid')

class AddUserForm(forms.Form):
    username = forms.CharField(required=True)
    email = EmailField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)
    groups = forms.ModelMultipleChoiceField(required=False, queryset=Group.objects.all())

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('A user with that username already exists.', code='invalid')

        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('A user with that email already exists.', code='invalid')

        return email
