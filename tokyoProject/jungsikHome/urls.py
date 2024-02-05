from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

from django.urls import path, include, reverse_lazy
from .views import IndexAPIView, LoginPageAPIView, index

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('api/index/', IndexAPIView.as_view(), name='api_index'),
    path('api/login/', LoginPageAPIView.as_view(), name='api_login_page'),
    path('', index, name='index'), 
    path('login/', auth_views.LoginView.as_view(template_name='jungsikHome/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('resume:resume_page')), name='logout'),
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
