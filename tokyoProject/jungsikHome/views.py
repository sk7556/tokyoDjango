from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required


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
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # 로그인 성공 시 리다이렉트 또는 다른 동작 수행
            return redirect('afterLogin')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    # 로그아웃 후 리다이렉트 또는 다른 동작 수행
    return redirect('afterLogout')


@login_required
def afterLogin(request):
    # 로그인한 사용자만 접근 가능한 뷰
    pass

def afterLogout(request):
    pass

@permission_required('some_app.can_view_content')
def restricted_view(request):
    # 특정 권한이 있는 사용자만 접근 가능한 뷰
    pass
