from django.shortcuts import render
from .form import contact_form
from .models import user_Table

# Create your views here.
def home(req):
    return render(req, 'home.html')

def about(req):
    return render(req, 'about.html')

def work(req):
    return render(req, 'work.html')

def contact(request):
    if request.method == "Post":
        form = contact_form(request.post)
        if form.is_valid():
            form.save()
        return render(request, 'thankyou.html')
    else:
        form = contact_form()
        return render(request, 'contact.html', {'form': form})

def thankyou(req):
    return render(req, 'thankyou.html')