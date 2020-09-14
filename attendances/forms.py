# import form class from django
from django import forms

# import Attendances from models.py
from .models import Attendances


# create a ModelForm
#Created this form following this tutorial https://tutorial.djangogirls.org/en/django_forms/
class AttendanceForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Attendances
        fields = "__all__"