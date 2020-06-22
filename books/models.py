from django.db import models
from jsonfield import JSONField

class Book(models.Model):
  # title = models.CharField(max_length=200)
  # author = models.CharField(max_length=200)
  # description = models.CharField(max_length=200)
  # owner = models.IntegerField()

  title = models.CharField(max_length=200)
  description = models.TextField()
  api_id = models.CharField(max_length=200)
  authors = models.CharField(max_length=200)
  industryIdentifiers = models.CharField(max_length=200)
  pageCount = models.IntegerField()
  mainCategory = models.CharField(max_length=200)
  categories = models.CharField(max_length=200)
  infoLink = models.CharField(max_length=200)
  averageRating = models.FloatField()
  ratingsCount = models.IntegerField()
  owner = models.IntegerField()

  def __str__(self):
    return self