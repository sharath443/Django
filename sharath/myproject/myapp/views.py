from django.shortcuts import render,HttpResponse

def mainpage(request):
    return render(request,'myhtml.html')
