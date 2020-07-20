from django import forms
from phonenumber_field.formfields import PhoneNumberField
import wiawdp.widgets as widgets
from wiawdp.formfields import ZIPCodeField, SSNField, EmailField
from wiawdp.models import Contract, WIAWDP


class AddContractForm(forms.ModelForm):
    end_date = forms.DateTimeField(widget=widgets.DateTimePickerWidget())

    class Meta:
        model = Contract
        fields = ['client', 'workforce', 'end_date', 'performance']


class ViewReportForm(forms.Form):
    start_date = forms.DateField(label="From", widget=widgets.DatePickerWidget())
    end_date = forms.DateField(label="To", widget=widgets.DatePickerWidget())
    locations = forms.MultipleChoiceField(choices=WIAWDP.LOCATION_CHOICES, widget=forms.CheckboxSelectMultiple)

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if end_date < start_date:
            raise forms.ValidationError('Please enter a valid date range.')


class FindStudentForm(forms.Form):
    first_name = forms.CharField(max_length=200, required=False)
    last_name = forms.CharField(max_length=200, required=False)
    ssn = SSNField(label='SSN', max_length=11, required=False)
    email = EmailField(required=False)
    home_phone = PhoneNumberField(required=False)
    cell_phone = PhoneNumberField(required=False)
    zipcode = ZIPCodeField(label='ZIP code', required=False)

    def clean(self):
        if not self.has_changed():
            raise forms.ValidationError('At least one field must be filled out.')


class ModifyContractLookupForm(forms.Form):
    student_id = forms.IntegerField()


class ModifyContractForm(forms.ModelForm):
    end_date = forms.DateTimeField(widget=widgets.DateTimePickerWidget())

    class Meta:
        model = Contract
        exclude = ['client']
