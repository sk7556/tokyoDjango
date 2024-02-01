from django import forms
from bootstrap_datepicker_plus import DatePickerInput
from .models import Diary

class diaryCalendar(forms.ModelForm):
    date_field = forms.DateField(
        widget=DatePickerInput(
            options={
                "format": "YYYY-MM-DD",  # 형식을 원하는대로 설정
                "showClose": True,
                "locale": "ko",  # 한글로 설정
            }
        )
    )

    class Meta:
        model = Diary
        fields = '__all__'
