from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render

class IndexAPIView(APIView):
    def get(self, request):
        return Response({"message": "Hello, this is the index API."})

class LoginPageAPIView(APIView):
    def get(self, request):
        return Response({"message": "This is the login page API."})

def index(request):
    return render(request, "jungsikHome/index.html")

def login_page(request):
    return render(request, "jungsikHome/login.html")
