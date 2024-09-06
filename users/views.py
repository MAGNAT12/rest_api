from django.shortcuts import render
from rest_framework import generics
from .models import Users
from .serializers import *
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
from rest_framework import status
from drf_spectacular.utils import extend_schema

@extend_schema(request=None, responses=None)
class User_all(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    http_method_names = ['get']

    def get(self, request):
        users = Users.objects.all().values()
        return Response({'users':list(users)})

@extend_schema(request=None, responses=None)
class User_create(generics.CreateAPIView):
    serializer_class = User_create
    http_method_names = ['post']

    def post(self, request):
        username = request.data['name'],
        password = request.data['password']
        if Users.objects.filter(name=username).exists():
            return Response({'message':'such a name already exists'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            Users.objects.create(name=username, password=password)
            return Response({'message':'successfully'}, status=status.HTTP_200_OK)

@extend_schema(request=None, responses=None)
class User_delete(generics.DestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = User_delet
    lookup_field = 'id'
    http_method_names = ['delete']

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'successfully'}, status=status.HTTP_200_OK)
    
@extend_schema(request=None, responses=None)
class User_put(generics.UpdateAPIView):
    serializer_class = User_put
    http_method_names = ['put']

    def put(self, request):
        username = request.data['name']
        userpassword = request.data['password']
        name_new = request.data['name_new']
        password_new = request.data['password_new']
        user = Users.objects.get(name=username)
        if user.name == username:
            if check_password(userpassword, user.password):
                user.name = name_new
                user.password = password_new
                user.save()
                return Response({'message': 'successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'the password is incorrect'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'name not found'}, status=status.HTTP_404_NOT_FOUND)