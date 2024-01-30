from rest_framework import viewsets
from .models import Resume
from .serializers import ResumeSerializer
from rest_framework.permissions import AllowAny
from django.shortcuts import render, get_object_or_404

class ResumeAPIView(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [AllowAny]    
    
def resume_page(request):
    return render(request, "resume/resume.html")

def update_resume(request, resume_id):
    resume = get_object_or_404(Resume, pk=resume_id)
    return render(request, 'update_resume.html', {'resume': resume})

