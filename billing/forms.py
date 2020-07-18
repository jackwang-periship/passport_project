from django import forms
from .models import Transaction, VerifiedId, Report
from django.utils import timezone

'''
class VerificationForm(forms.Form):
    firstName = forms.CharField(max_length=14, help_text='First Name:')
    lastName = forms.CharField(max_length=18, help_text='Last Name: ')
    studentId = forms.IntegerField(help_text='Record ID: ', initial=12345)
    dateOfBirth = forms.DateField(initial=timezone.now, )

    def clean_studentId(self):
        studentId = self.cleaned_data.get("studentId")
        if studentId < 0:
            raise forms.ValidationError("Student ID must be a positive number")
        if studentId > 100000:
            raise forms.ValidationError("Student ID must be comprised of 5 digits")
        return studentId


class PaymentInfoForm(forms.Form):
    firstName = forms.CharField(max_length=14, help_text='First Name:')
    lastName = forms.CharField(max_length=18, help_text='Last Name: ')
    address = forms.CharField(max_length=50, help_text='Address: ')
    city = forms.CharField(max_length=30, )
    state = forms.CharField(max_length=13, )
    zipcode = forms.IntegerField(help_text='ZIP code: ')
    phone = forms.CharField(max_length=15, )
'''


class VerifiedIdForm(forms.ModelForm):
    studentId = forms.IntegerField(help_text='Record ID: ', widget=forms.TextInput(attrs={"placeholder": "12345"}))

    class Meta:
        model = VerifiedId
        fields = ('studentId',)

    def __init__(self, *args, **kwargs):
        super(VerifiedIdForm, self).__init__(*args, **kwargs)
        self.fields['studentId'].required = False

    def clean_studentId(self):
        studentId = self.cleaned_data.get("studentId")
        if studentId < 0:
            raise forms.ValidationError("Student ID must be a positive number")
        if studentId > 100000:
            raise forms.ValidationError("Student ID must be comprised of 5 digits")
        return studentId


class TransactionForm(forms.ModelForm):
    verifiedId = forms.IntegerField(help_text='Record ID: ', initial=12345)
    firstName = forms.CharField(max_length=14, help_text='First Name:')
    lastName = forms.CharField(max_length=18, help_text='Last Name: ')
    counselor = forms.CharField(max_length=24, help_text='Counselor: ')
    course = forms.CharField(max_length=32, help_text='Course: ')
    balance = forms.DecimalField(max_digits=8, decimal_places=2, help_text='Balance: ')

    class Meta:
        model = Transaction
        fields = ('verifiedId', 'firstName', 'lastName', 'counselor', 'course', 'balance')
        # exclude = ('verifiedId',)

    def clean_verifiedId(self):
        verifiedId = self.cleaned_data.get("verifiedId")
        if verifiedId < 0:
            raise forms.ValidationError("Student ID must be a positive number")
        if verifiedId > 100000:
            raise forms.ValidationError("Student ID must be comprised of 5 digits")
        return verifiedId


class ReportForm(forms.ModelForm):
    TYPE_CHOICES = (
        ("payment", "By Payment"),
        ("location", "By Location"),
        ("counselor", "By Counselor"),
        ("course", "By Course"),
    )
    startD = forms.DateField(help_text='Select Start Date', initial=timezone.now(),
                             widget=forms.DateInput(attrs={'type': 'date'}))
    endD = forms.DateField(help_text='Select End Date', initial=timezone.now(),
                           widget=forms.DateInput(attrs={'type': 'date'}))
    type = forms.CharField(max_length=12, widget=forms.Select(choices=TYPE_CHOICES), help_text='Report Type: ')

    class Meta:
        model = Report
        fields = ('startD', 'endD', 'type')
