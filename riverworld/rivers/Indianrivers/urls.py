from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('river',views.river),
    path('about',views.about),
]
