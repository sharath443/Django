from django.shortcuts import render,HttpResponse

from datetime import datetime

def timer3(request):
    now = datetime.now()
    t = now.strftime("%H:%M:%S")
    s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
    s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
    return HttpResponse(f"{t}<br>{s1}<br>{s2}")



