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


class FindStudentForm(forms.Form):
    first_name = forms.CharField(max_length=200, required=False)
    last_name = forms.CharField(max_length=200, required=False)
    ssn = forms.CharField(label='SSN', max_length=11, required=False,
                          widget=widgets.InputMaskWidget(attrs={'autocomplete': 'off', 'data-inputmask-alias': 'ssn'}))
    email = forms.EmailField(required=False, widget=widgets.InputMaskWidget(
        attrs={'autocomplete': 'off', 'data-inputmask-alias': 'email'}))
    home_phone = PhoneNumberField(required=False)
    cell_phone = PhoneNumberField(required=False)
    zipcode = forms.CharField(max_length=20, required=False,
                              widget=widgets.InputMaskWidget(
                                  attrs={'autocomplete': 'off', 'data-inputmask-mask': '99999'}))

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
