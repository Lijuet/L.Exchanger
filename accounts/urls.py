from django.urls import include, path
from rest_framework import routers  # router import
from . import views  # views.py import

router = routers.DefaultRouter()
# router.register(r'', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = [
#     path('google/login', views.google_login, name='google_login'),
#     path('google/callback/', views.google_callback,      name='google_callback'),  
#    path('accounts/google/login/finish/', views.GoogleLogin.as_view(), name='google_login_todjango'),
# ]