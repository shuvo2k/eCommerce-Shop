from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'bookfinder'

urlpatterns = [
    path('all', views.test, name='test'),
    #path('all/', views.SearchProduct.as_view(), name='search book'),
    ]
