from django.urls import path
from .views import PageView, PageList

from . import views

urlpatterns = [
  path('', PageList.as_view()),
  path('<int:pk>/', PageView.as_view())
]