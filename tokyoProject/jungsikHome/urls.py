from django.conf.urls.static import static
from django.conf import settings

from django.urls import path, include
from .views import IndexAPIView, LoginPageAPIView, index, login_view, logout_view


urlpatterns = [
    path('api/index/', IndexAPIView.as_view(), name='api_index'),
    path('api/login/', LoginPageAPIView.as_view(), name='api_login_page'),
    path('', index, name='index'), 
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    # 외부 앱 연결 
    path('todo/', include('toDo.urls')),
    path('resume/', include('resume.urls')),
    path('diary/', include('diary.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
