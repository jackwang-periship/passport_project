from django import forms
from .models import Transaction, VerifiedId, Report
from django.utils import timezone

class VerifiedIdForm(forms.ModelForm):
    studentId = forms.IntegerField(help_text='Record ID: ', widget=forms.TextInput(attrs={"placeholder": "12345"}))

    class Meta:
        model = VerifiedId
        fields = ('studentId',)

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
    date = forms.DateField(widget=forms.HiddenInput(), initial=timezone.now)

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
    startD = forms.DateField(help_text='Select Start Date', initial=timezone.now())
    endD = forms.DateField(help_text='Select End Date', initial=timezone.now())
    type = forms.CharField(max_length=12, widget=forms.Select(choices=TYPE_CHOICES), help_text='Report Type: ')

    class Meta:
        model = Report
        fields = ('startD', 'endD', 'type')