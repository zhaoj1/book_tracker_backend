from django.urls import path
from .views import BookView, BookList, UpdateBookView

from . import views

urlpatterns = [
  path('<int:pk>/', BookView.as_view()),
  path('<int:pk>/patch/', UpdateBookView.as_view()),
  path('', BookList.as_view()),
]