from django.urls import path
from .views import BookView, BookList

from . import views

# urlpatterns = [
#   path('', views.ListBook.as_view()),
#   path('<int:pk>/', views.DetailBook.as_view()),
# ]
urlpatterns = [
  path('<int:pk>/', BookView.as_view()),
  path('', BookList.as_view())
]