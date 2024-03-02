from django.conf.urls.static import static
from django.conf import settings

from django.urls import path, include
from .views import IndexAPIView, LoginPageAPIView, index, login_view, logout_view

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('api/index/', IndexAPIView.as_view(), name='api_index'),
    path('api/login/', LoginPageAPIView.as_view(), name='api_login_page'),
    path('', index, name='index'), 
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    # 토큰 api 관련 설정 
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # 외부 앱 연결 
    path('todo/', include('toDo.urls')),
    path('resume/', include('resume.urls')),
    path('diary/', include('diary.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
