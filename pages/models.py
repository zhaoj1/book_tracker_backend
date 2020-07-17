from django.db import models

class Page(models.Model):

  pagesRead = models.IntegerField()
  dateOf = models.DateField()
  book = models.IntegerField()
  user = models.IntegerField()

  def __str__(self):
    return self