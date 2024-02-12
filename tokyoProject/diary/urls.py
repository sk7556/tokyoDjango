# File: urls.py
from django.urls import path
from .views import DiaryEntryListView, DiaryEntryCreateView

app_name = 'diary'

urlpatterns = [
    path('', DiaryEntryListView.as_view(), name='entry_list'),
    path('create/', DiaryEntryCreateView.as_view(), name='entry_create'),
]
