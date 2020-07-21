from django.db import models

class Page(models.Model):

  pagesRead = models.IntegerField()
  dateRead = models.CharField(max_length=10)
  book = models.IntegerField()
  owner = models.IntegerField()
  username = models.CharField(max_length=200)

  def __str__(self):
    return self