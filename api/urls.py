from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('room', room.as_view(), name='index'),
    path('details/<int:pk>', detail.as_view(), name='detailsview'),
]