import datetime

from django.shortcuts import render,HttpResponse

def timer1(request):
    date = datetime.datetime.now()
    return HttpResponse(f'prasent time: {date}')

