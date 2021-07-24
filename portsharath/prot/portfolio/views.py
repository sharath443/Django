from django.shortcuts import render
from .forms import contact_form
from .models import user_Table

# Create your views here.
def home(req):
    return render(req, 'home.html')

def about(req):
    return render(req, 'about.html')

def work(req):
    return render(req, 'work.html')

def contact(request):
    if request.method == "POST":
        form = contact_form(request.POST)
        if form.is_valid():
            data = user_Table(name=form.cleaned_data['name'],email= form.cleaned_data['email'],txt= form.cleaned_data['txt'])
            data.save()
        return render(request, 'thankyou.html')
    else:
        form = contact_form()
        return render(request, 'contact.html', {'form': form})

def thankyou(req):
    return render(req, 'thankyou.html')