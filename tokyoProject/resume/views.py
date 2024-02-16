from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Resume
from .serializers import ResumeSerializer

class ResumeAPIView(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        return self.queryset.first()
    
def resume_page(request):
    resume = Resume.objects.first()
    return render(request, "resume/resume.html", {'resume': resume})

@login_required(login_url='/login/')
def update_resume(request):
    resume = Resume.objects.first()
    if request.user.is_authenticated:
        return render(request, 'resume/update_resume.html', {'resume': resume})
    else:
        return HttpResponse("로그인 된 사용자만 사용 가능합니다.", status=403)