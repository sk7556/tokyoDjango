from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect

class IndexAPIView(APIView):
    def get(self, request):
        return Response({"message": "Hello, this is the index API."})

class LoginPageAPIView(APIView):
    def get(self, request):
        return Response({"message": "This is the login page API."})

def index(request):
    return render(request, "jungsikHome/index.html")

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next') or 'resume:resume_page'
            return HttpResponseRedirect(next_url)
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        next_url = request.GET.get('next') or 'resume:resume_page'
    return render(request, 'login.html', {'next': next_url})

def logout_view(request):
    logout(request)
    return redirect('resume:resume_page') 

