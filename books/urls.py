from django.urls import path

from . import views

urlpatterns = [
  path('', views.ListBook.as_view()),
  path('<int:pk>/', views.DetailBook.as_view()),
]