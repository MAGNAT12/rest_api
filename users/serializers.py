from rest_framework import serializers
from .models import Users

class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = Users
        fields = "__all__"
    

class User_delet(serializers.ModelSerializer):
    class Meta():
        model = Users
        fields = ['id']


class User_create(serializers.ModelSerializer):
    class Meta():
        model = Users
        fields = ['name', 'password']

class User_put(serializers.ModelSerializer):
    class Meta():
        model = Users
        fields = ['name', 'password']