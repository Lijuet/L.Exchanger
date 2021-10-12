from django.urls import include, path
from rest_framework import routers  # router import
from . import views  # views.py import


router = routers.DefaultRouter()
router.register(r'', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)), 
]
