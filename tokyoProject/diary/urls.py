from django.urls import path
from .views import DiaryDateSelectionAPIView, DiaryDetailAPIView

app_name = 'diary'

urlpatterns = [
    path('api/diary/date_selection/', DiaryDateSelectionAPIView.as_view(), name='api_diary_date_selection'),
    path('api/diary/<int:year>/<int:month>/<int:day>/', DiaryDetailAPIView.as_view(), name='api_diary_detail'),
    path('date_selection/', DiaryDateSelectionAPIView.as_view(), name='diary_date_selection'),
    path('<int:year>/<int:month>/<int:day>/', DiaryDetailAPIView.as_view(), name='diary_detail'),
]
