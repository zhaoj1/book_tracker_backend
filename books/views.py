from django.shortcuts import render

from rest_framework import generics

from .models import Book
from .serializers import BookSerializer

class ListBook(generics.ListCreateAPIView):

  # def get_queryset(self):
  #   user = self.request.user
  #   return Book.objects.filter(owner=user)

  queryset = Book.objects.all()
  serializer_class = BookSerializer

class DetailBook(generics.RetrieveUpdateDestroyAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer

# from django.http import HttpResponseRedirect
# from rest_framework import permissions, status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .serializers import BookSerializer, BookSerializerWithToken

# @api_view(['GET'])
# def current_book(request):
#   serializer = BookSerializer(request.book)
#   return Response(serializer.data)

# class BookList(APIView):
#   permission_classes = (permissions.AllowAny,)

#   def post(self, request, format=None):
#     serializer = BookSerializerWithToken(data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)