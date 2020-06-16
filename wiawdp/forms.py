from django import forms

# class ActiveContractForm(forms.ModelForm):
#     # client = forms.ModelChoiceField(queryset=Pclient.objects.all())
#     # work_force = forms.CharField()
#     end_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
#     class Meta:
#         model = Contract
#         exclude = []
# class ModifyContractForm(forms.Mode)

class ViewReportForm(forms.Form):
    start_date = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'date'}))
    eatontown = forms.BooleanField(required=False)
    fairfield = forms.BooleanField(required=False)
    south_plainfield = forms.BooleanField(required=False)
    # location = forms.ModelChoiceField(Location.objects.all())

class FindStudentForm(forms.Form):
    first_name = forms.CharField(max_length=200, required=False)
    last_name = forms.CharField(max_length=200, required=False)
    ssn = forms.CharField(max_length=11, required=False)
    email = forms.EmailField(required=False)
    home_phone = forms.CharField(max_length=50, required=False)
    cell_phone = forms.CharField(max_length=50, required=False)
    zipcode = forms.CharField(max_length=20, required=False)

class ModifyContractLookupForm(forms.Form):
    student_id = forms.UUIDField()