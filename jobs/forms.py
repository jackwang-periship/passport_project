# ALL FIELDS FROM DOCS
# 'Field', 'CharField', 'IntegerField',
# 'DateField', 'TimeField', 'DateTimeField', 'DurationField',
# 'RegexField', 'EmailField', 'FileField', 'ImageField', 'URLField',
# 'BooleanField', 'NullBooleanField', 'ChoiceField', 'MultipleChoiceField',
# 'ComboField', 'MultiValueField', 'FloatField', 'DecimalField',
# 'SplitDateTimeField', 'GenericIPAddressField', 'FilePathField',
# 'JSONField', 'SlugField', 'TypedChoiceField', 'TypedMultipleChoiceField',
# 'UUIDField',

from django import forms
from .models import Posting, Client
import datetime

class PostingForm(forms.ModelForm):
    title = forms.CharField(label='Job Title', max_length=64, widget=forms.TextInput(attrs={'size':'30', 'placeholder': 'Job title'}))
    position = forms.CharField(label='Job Title', max_length=64, widget=forms.TextInput(attrs={'size':'30', 'placeholder': 'Position'}))
    location = forms.CharField(label='Location', max_length=64, widget=forms.TextInput(attrs={'size':'30', 'placeholder': 'address'}))
    deadline = forms.DateField(label='Deadline', widget=forms.DateInput(format=('%d-%m-%Y'), attrs={'class':'myDateClass', 'placeholder':'YYYY-MM-DD'}))

    class Meta:
        model=Posting
        fields=(
        'title',
        'location',
        'deadline',
        'position',
        )