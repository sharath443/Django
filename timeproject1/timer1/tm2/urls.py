from django.urls import path
from . import views

urlpatterns = [
    path('',views.timer1,name="now_time"),

]