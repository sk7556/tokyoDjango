from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .models import Resume
from .serializers import ResumeSerializer

class ResumeAPIView(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

    def get_permissions(self):
        # if self.action == 'retrieve':
        permission_classes = [AllowAny]
        # else:
            # permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_object(self):
        return self.queryset.first()
    
def resume_page(request):
    resume = Resume.objects.first()
    return render(request, "resume/resume.html", {'resume': resume})

def update_resume(request):
    resume = Resume.objects.first()
    return render(request, 'resume/update_resume.html', {'resume': resume})

update_resume = permission_classes([IsAuthenticated])(update_resume)
