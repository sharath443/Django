from django.urls import path
from . import views

urlpatterns = [
    path('',views.timer2,name="tmrw_time"),

]