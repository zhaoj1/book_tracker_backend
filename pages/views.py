from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Page
from .serializers import PageSerializerWithToken

class PageView(APIView):

  permission_classes = [permissions.AllowAny]
  http_method_names = ['get', 'head', 'post']

  def get(self, request, pk):
    page = get_object_or_404(Page.objects.all(),pk=pk)
    serializer = PageSerializerWithToken(page)
    return Response(serializer.data)
  
  def delete(self, request, pk):
    page = get_object_or_404(Page.objects.all(),pk=pk)
    page.delete()

class PageList(APIView):

  def get(self, request): 
    pages = list(filter(lambda x: x.owner == request.user.id, Page.objects.all()))
    serializer = PageSerializerWithToken(pages, many=True)
    return Response({'pages':serializer.data})

  def post(self, request, format=None):
    serializer = PageSerializerWithToken(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)