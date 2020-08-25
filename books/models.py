from django.db import models

class Book(models.Model):

  title = models.CharField(max_length=200)
  api_id = models.CharField(max_length=200)
  authors = models.CharField(max_length=200)
  imageLink = models.CharField(max_length=200)
  isbn10 = models.CharField(max_length=200)
  isbn13 = models.CharField(max_length=200)
  owner = models.IntegerField()
  username = models.CharField(max_length=200)
  totalPages = models.IntegerField()
  completed = models.BooleanField()

  def __str__(self):
    return self