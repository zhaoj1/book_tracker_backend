from django.urls import path
from .views import BookView, BookList, PageView

from . import views

urlpatterns = [
  path('<int:pk>/', BookView.as_view()),
  path('', BookList.as_view()),
  path('<int:pk>/pages', PageView.as_view())
]