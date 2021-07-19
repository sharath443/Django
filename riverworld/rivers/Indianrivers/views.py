from django.shortcuts import render
def home(request):
    return render(request,"home.html")

# Create your views here.
def river(request):
    return render(request,"indian Rivers.html")
def about(request):
    return render(request,"about_support.html")