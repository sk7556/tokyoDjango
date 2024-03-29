from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet
from django.shortcuts import render

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

app_name = 'toDo'

def toDo_page(request):
    return render(request, 'toDo/toDo.html')

urlpatterns = [
    path('', toDo_page, name='toDo'),
    path('api/', include(router.urls)),  # /api/posts/ 형태로 변경
]
