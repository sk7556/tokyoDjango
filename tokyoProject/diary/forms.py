# forms.py
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django import forms
from .models import DiaryEntry

class DiaryEntryForm(forms.ModelForm):
    class Meta:
        model = DiaryEntry
        exclude = ['pub_date']

    pub_date = forms.DateTimeField(
        widget=DateTimePickerInput(),
    )
