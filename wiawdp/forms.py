from django import forms
from phonenumber_field.formfields import PhoneNumberField
import wiawdp.widgets as widgets
from wiawdp.models import Contract


class AddContractForm(forms.ModelForm):
    end_date = forms.DateTimeField(widget=widgets.DateTimePickerWidget())

    class Meta:
        model = Contract
        fields = ['client', 'workforce', 'end_date', 'performance']


class ViewReportForm(forms.Form):
    start_date = forms.DateField(label="From", widget=widgets.DatePickerWidget())
    end_date = forms.DateField(label="To", widget=widgets.DatePickerWidget())
    eatontown = forms.BooleanField(required=False)
    fairfield = forms.BooleanField(required=False)
    south_plainfield = forms.BooleanField(required=False, label='South Plainfield')

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if end_date < start_date:
            raise forms.ValidationError('Please enter a valid date range.')

        if not any([cleaned_data.get('eatontown'), cleaned_data.get('fairfield'), cleaned_data.get('south_plainfield')]):
            raise forms.ValidationError('Please select at least one location.')


def validate_ssn(value):
    cleaned = value.replace('-', '')
    if len(cleaned) != 9 or not cleaned.isdigit():
        raise forms.ValidationError('Please enter a valid SSN.')


def validate_zip_code(value):
    if len(value) != 5 or not value.isdigit():
        raise forms.ValidationError('Please enter a valid ZIP code.')


class FindStudentForm(forms.Form):
    first_name = forms.CharField(max_length=200, required=False)
    last_name = forms.CharField(max_length=200, required=False)
    ssn = forms.CharField(label='SSN', max_length=11, required=False, validators=[validate_ssn],
                          widget=widgets.InputMaskWidget(attrs={'autocomplete': 'off', 'data-inputmask-alias': 'ssn'}))
    email = forms.EmailField(required=False, widget=widgets.InputMaskWidget(
        attrs={'autocomplete': 'off', 'data-inputmask-alias': 'email'}))
    home_phone = PhoneNumberField(required=False)
    cell_phone = PhoneNumberField(required=False)
    zipcode = forms.CharField(label='ZIP code', max_length=20, required=False, validators=[validate_zip_code],
                              widget=widgets.InputMaskWidget(
                                  attrs={'autocomplete': 'off', 'data-inputmask-mask': '99999'}))

    def clean(self):
        if not self.has_changed():
            raise forms.ValidationError('At least one field must be filled out.')

    def clean_ssn(self):
        ssn = self.cleaned_data.get('ssn')
        return ssn.replace('-', '')


class ModifyContractLookupForm(forms.Form):
    student_id = forms.IntegerField()


class ModifyContractForm(forms.ModelForm):
    end_date = forms.DateTimeField(widget=widgets.DateTimePickerWidget())

    class Meta:
        model = Contract
        exclude = ['client']
