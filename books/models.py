from django.db import models
from jsonfield import JSONField

class Book(models.Model):
  # title = models.CharField(max_length=200)
  # author = models.CharField(max_length=200)
  # description = models.CharField(max_length=200)
  # owner = models.CharField(max_length=5)
  json = JSONField()
  owner = models.IntegerField()

  def __str__(self):
    return self