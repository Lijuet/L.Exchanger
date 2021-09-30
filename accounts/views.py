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

    
    @action(detail=False, methods=['post'])
    def signup(self, request):
        info = UserSerializer(data=request.data)
        if info.is_valid():
            User.objects.create_user(
                email=request.data.get('email'),
                username=request.data.get('username'),
                password=request.data.get('password'),
                main_language=request.data.get('main_language'),
                study_language=request.data.get('study_language'),
                goal=request.data.get('goal')
            )
            return JsonResponse(info.data, status=status.HTTP_200_OK)
        else:
            return JsonResponse(info._errors, status=status.HTTP_400_BAD_REQUEST)

    def get_permissions(self):
        try:
            if self.action == "list":
                return [permission() for permission in self.permission_classes_by_action[self.action]]
            else:
                return [permission() for permission in self.permission_classes_by_action['basic']]
        except:
            return [permission() for permission in self.permission_classes]
