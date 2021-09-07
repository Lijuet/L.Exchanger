from rest_framework import viewsets

# Create your views here.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserCreateSerializer
#     permission_classes = [AllowAny]

#     @action(detail=False, methods=['post'])
#     # @permission_classes([AllowAny])
#     def login(self, request):

#         """
#         Login Info
#         """
#         email = request.data['email']
#         password = request.data['password']