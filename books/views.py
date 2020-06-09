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