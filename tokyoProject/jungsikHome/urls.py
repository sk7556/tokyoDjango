from django.urls import path, include
from .views import IndexAPIView, LoginPageAPIView, index, login_page

urlpatterns = [
    path('api/index/', IndexAPIView.as_view(), name='api_index'),
    path('api/login/', LoginPageAPIView.as_view(), name='api_login_page'),
    path('api/v1/', index, name='index'), # api/v1/ 에 대한 정의가 필요하다는 GPT의 억지에 타보
    path('', index, name='index'), 
    path('login/', login_page, name='login_page'),
    # 외부 앱 연결 
    path('todo/', include('toDo.urls')),
    path('resume/', include('resume.urls')),
    path('diary/', include('diary.urls')),
]
