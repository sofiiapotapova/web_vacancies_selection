from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('user-page', views.users_page, name='user'),
    path('search-results', views.search_results, name='search'),
    path('sign', views.sign, name='sign'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),

]
