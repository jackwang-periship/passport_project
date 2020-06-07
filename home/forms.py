from django.contrib.auth.models import User
from django import forms
from .models import UserProfile
from .models import USER_TYPE_CHOICES

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
