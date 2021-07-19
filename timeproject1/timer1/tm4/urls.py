from django.urls import path
from . import views

urlpatterns = [
    path('',views.timer3,name="all_time"),

]