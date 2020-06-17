from django.urls import path
# from .views import current_book, BookList

from . import views

urlpatterns = [
  path('', views.ListBook.as_view()),
  path('<int:pk>/', views.DetailBook.as_view()),
]
# urlpatterns = [
#   path('<int:pk>/', current_book),
#   path('books/', BookList.as_view())
# ]