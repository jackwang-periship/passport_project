from django import forms
from phonenumber_field.formfields import PhoneNumberField

class ViewReportForm(forms.Form):
    start_date = forms.DateField(label="From")
    end_date = forms.DateField(label="To")
    eatontown = forms.BooleanField(required=False)
    fairfield = forms.BooleanField(required=False)
    south_plainfield = forms.BooleanField(required=False, label='South Plainfield')


class FindStudentForm(forms.Form):
    first_name = forms.CharField(max_length=200, required=False)
    last_name = forms.CharField(max_length=200, required=False)
    ssn = forms.CharField(max_length=11, required=False)
    email = forms.EmailField(required=False)
    home_phone = PhoneNumberField(required=False)
    cell_phone = PhoneNumberField(required=False)
    zipcode = forms.CharField(max_length=20, required=False)


class ModifyContractLookupForm(forms.Form):
    student_id = forms.IntegerField()
