import json
from json.encoder import JSONEncoder
from django.db.models import query
from django.core import serializers
from django.http.response import HttpResponse
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
import requests

from django.http import JsonResponse

from .models import Group, User
from .serializer import GroupSerializer

# Create your views here.
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    @action(detail=False, methods=['post'])
    def autoMatch(self, request):
        '''
        # Input
        1. email : get user's main_language with the email
        2. study_language

        # Output
        1. list of user
            -study_lanugage = request's main_language
            -main_lanugae == request'study language
        '''
        email = request.data["email"]
        study_language = request.data["studyLanguage"]
        
        if User.objects.filter(email=email).exists():
            main_language = User.objects.get(email=email).main_language
        else:
            return JsonResponse({"err_msg":"There is no user with such email"}, status=status.HTTP_404_NOT_FOUND)
        
        queryset = User.objects.filter(main_language=study_language, study_language=main_language).values('username','email','main_language', 'study_language', 'goal')
        serialized_response = json.dumps(list(queryset))
        return JsonResponse({"result": serialized_response}, status=status.HTTP_200_OK)
    

    @action(detail=False, methods=['post'])
    def studyGroup(self, request):
        info = GroupSerializer(data=request.data)
        if info.is_valid():
            Group.objects.create_group("study_group_test", request.data["studyLanguages"], request.data["wishMembers"]
            )
            return JsonResponse(info.data, status=status.HTTP_200_OK)
        else:
            return JsonResponse(info._errors, status=status.HTTP_400_BAD_REQUEST)