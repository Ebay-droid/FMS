from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from datetime import datetime
# Create your views here.

@api_view(['GET'])
def index(request):
  date = datetime.now().strftime("%d/%m/%Y  %H:%M:%S")
  message = 'server is live at current time'
  return Response(data=message + date,status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes(IsAuthenticated)
def restricted(request,*args,**kwargs):
  return Response(data="Only for logged in users", status=status.HTTP_200_OK)