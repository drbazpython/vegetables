from django.contrib import admin
from django.urls import path
from .views import vegetables_home_view, vegetables_add_view,vegetables_list_view

urlpatterns = [
    path('', vegetables_home_view, name='home'),
    path('add/', vegetables_add_view, name='add'),
    path('list/<id>', vegetables_list_view, name='list'),
]
