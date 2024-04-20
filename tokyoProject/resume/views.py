from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
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

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def update_resume(request):
    resume = Resume.objects.first()
    if request.method == 'POST':
        # Update the resume here
        pass
    return render(request, 'resume/update_resume.html', {'resume': resume})
