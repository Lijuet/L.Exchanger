from django.urls import include, path
from rest_framework import routers  # router import
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views  # views.py import


router = routers.DefaultRouter()
router.register(r'', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)), 
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# urlpatterns = [
#     path('google/login', views.google_login, name='google_login'),
#     path('google/callback/', views.google_callback,      name='google_callback'),  
#    path('accounts/google/login/finish/', views.GoogleLogin.as_view(), name='google_login_todjango'),
# ]