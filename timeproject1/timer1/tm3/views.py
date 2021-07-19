from django.shortcuts import render

import datetime

from django.shortcuts import render,HttpResponse

def timer2(request):
    date = datetime.datetime.today()
    return HttpResponse(f'prasent date: {date}')

