from django.db import models

class Page(models.Model):

  pagesRead = models.IntegerField()
  dateOf = models.CharField(max_length=10)
  book = models.IntegerField()
  owner = models.IntegerField()

  def __str__(self):
    return self