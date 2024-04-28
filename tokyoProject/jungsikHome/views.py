from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.shortcuts import render
from django.contrib import messages
from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
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
            tokens = get_tokens_for_user(user)
            response = Response(tokens)
            response.set_cookie(key="access", value=tokens['access'], httponly=True)
            response.set_cookie(key="refresh", value=tokens['refresh'], httponly=True)
            return response
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'login.html', {'next': request.POST.get('next', 'resume:resume_page')})
    else:
        return render(request, 'login.html', {'next': request.GET.get('next', 'resume:resume_page')})

def logout_view(request):
    response = Response({"message": "Logged out"})
    response.delete_cookie('access')
    response.delete_cookie('refresh')
    return response
