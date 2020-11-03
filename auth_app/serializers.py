from .models import  *
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, UserSerializer


class  UserCreateSerializer(UserCreateSerializer):
  class Meta(UserCreateSerializer.Meta):
    model = User
    fields = ('id','email','username', 'password','first_name','last_name')