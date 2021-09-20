from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
import requests

from django.http import JsonResponse

from .models import User
from .serializer import UserSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes_by_action = {'list':[IsAuthenticated], 'basic':[AllowAny]}

    @action(detail=False, methods=['post'])
    def login(self, request):

        """
        Login Info
        """
        email = request.data['email']
        password = request.data['password']

        """
        JWT Token
        """
        try:
            response = requests.post("http://127.0.0.1:8000/accounts/api/token/",  data={'email':email, 'password':password})
            access, refresh = response.json().get('access'), response.json().get('refresh')
            if access and refresh:
                return JsonResponse({'access':access, 'refresh':refresh }, status=status.HTTP_200_OK)
            return JsonResponse({'err_msg': "Incorrect email or password!"}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as err:
            return JsonResponse({'err_msg': "Incorrect email or password!"}, status=status.HTTP_401_UNAUTHORIZED)

    def get_permissions(self):
        try:
            if self.action in self.permission_classes_by_action.keys():
                return [permission() for permission in self.permission_classes_by_action[self.action]]
            else:
                return [permission() for permission in self.permission_classes_by_action['basic']]
        except:
            return [permission() for permission in self.permission_classes]
