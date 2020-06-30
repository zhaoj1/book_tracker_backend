from django.db import models
from jsonfield import JSONField
from django_mysql.models import ListTextField

class Book(models.Model):

  title = models.CharField(max_length=200)
  api_id = models.CharField(max_length=200)
  authors = models.CharField(max_length=200)
  imageLink = models.CharField(max_length=200)
  isbn10 = models.IntegerField()
  isbn13 = models.IntegerField()
  owner = models.IntegerField()
  username = models.CharField(max_length=200)

  def __str__(self):
    return self