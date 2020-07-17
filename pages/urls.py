from django.urls import path
from .views import PageView

from . import views

urlpatterns = [
  path('', PageView.as_view()),
]