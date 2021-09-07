from rest_framework import viewsets
from rest_framework.decorators import action
from .models import User
from .serializer import UserSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # @action(detail=False, methods=['post'])
    # # @permission_classes([AllowAny])
    # def login(self, request):

    #     """
    #     Login Info
    #     """
    #     email = request.data['email']
    #     password = request.data['password']