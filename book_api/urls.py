from django.contrib import admin
from django.urls import path
from book_api import views
urlpatterns = [
    path('list/', views.book_list),
    path('', views.book_create),
    path('<int:pk>/', views.book)
]
