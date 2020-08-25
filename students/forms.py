from django import forms
from .models import Student
from students.formfields import ZIPCodeField, SSNField, EmailField, PhoneNumberField
import students.widgets as widgets


class StudentForm(forms.ModelForm):
    ssn = SSNField()
    zipcode = ZIPCodeField()
    birth_date = forms.DateField(widget=widgets.DatePickerWidget())
    cellPhone = PhoneNumberField()
    email = EmailField()

    class Meta:
        model = Student
        fields = (
            'first_name', 'last_name', 'ssn', 'birth_date', 'homeAddress', 'country', 'city','zipcode', 'cellPhone', 'email',
            'location',
            'refer', 'sources', 'gender')


class SearchStudentForm(forms.Form):
    first_name = forms.CharField(max_length=20, required=False)
    last_name = forms.CharField(max_length=20, required=False)
    cellPhone = PhoneNumberField(required=False)
    email = EmailField(required=False)
    ssn = SSNField(required=False)
    address = forms.CharField(required=False)
    zipcode = ZIPCodeField(required=False)

    def clean(self):
        if not self.has_changed():
            raise forms.ValidationError('At least one field must be filled out.')


class ModifyStudentInfoForm(forms.ModelForm):
    ssn = SSNField()
    zipcode = ZIPCodeField()
    birth_day = forms.DateField(widget=widgets.DatePickerWidget())
    cellphone = PhoneNumberField()
    email = EmailField()

    class Meta:
        model = Student
        fields = (
            'first_name', 'last_name', 'ssn', 'birth_date', 'homeAddress', 'zipcode', 'country', 'city', 'cellPhone', 'email',
            'location',
            'refer', 'sources', 'gender')
