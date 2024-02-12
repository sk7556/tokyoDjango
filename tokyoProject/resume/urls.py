from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ResumeAPIView,resume_page, update_resume

app_name = 'resume'
router = DefaultRouter()
router.register(r'resumes', ResumeAPIView, basename='resume')

urlpatterns = [
    path('api/', include(router.urls)),
    path('', resume_page, name='resume_page'),
    path('update/', update_resume, name='update_resume'),
]
