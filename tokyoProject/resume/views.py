from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render

class ResumeAPIView(APIView):
    def get(self, request):
        return Response({"message": "This is the Resume API."})
    
def resume_page(request):
    return render(request, "resume/resume.html")

