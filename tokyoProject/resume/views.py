from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Resume
from .serializers import ResumeSerializer

class ResumeAPIView(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        # 항상 첫 번째 Resume 객체만을 반환합니다.
        return self.queryset.first()
    
def resume_page(request):
    # Resume 객체를 가져와 템플릿에 전달
    resume = Resume.objects.first()
    return render(request, "resume/resume.html", {'resume': resume})

def update_resume(request):
    # Resume 객체를 가져와 템플릿에 전달
    resume = Resume.objects.first()
    return render(request, 'resume/update_resume.html', {'resume': resume})

