from django.urls import path
from .views import ResumeAPIView,resume_page, update_resume

app_name = 'resume'

urlpatterns = [
    path('api/', ResumeAPIView.as_view(), name='api_resume'),
    path('', resume_page, name='resume_page'),
    path('resume/<int:resume_id>/update/', update_resume, name='update_resume'),
    
]
