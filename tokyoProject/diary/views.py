# File: views.py
from django.views import generic
from .models import DiaryEntry
from .forms import DiaryEntryForm

class DiaryEntryListView(generic.ListView):
    model = DiaryEntry
    template_name = 'diary/entry_list.html'  # 해당 템플릿 파일을 만들어주어야 합니다.

class DiaryEntryCreateView(generic.edit.CreateView):
    model = DiaryEntry
    form_class = DiaryEntryForm
    template_name = 'diary/entry_form.html'  # 해당 템플릿 파일을 만들어주어야 합니다.
    success_url = '/diary/'  # 성공 시 이동할 URL
