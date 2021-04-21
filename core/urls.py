from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('user-page', views.users_page, name = 'user')
]