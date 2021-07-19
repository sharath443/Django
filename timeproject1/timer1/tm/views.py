from django.shortcuts import render,HttpResponse
import datetime
def time(request):
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    return HttpResponse (f"yesterday date {yesterday}")
