from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'
        widgets = {'photo': forms.ClearableFileInput(attrs={'required': True})}
