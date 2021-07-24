from django import forms

class contact_form(forms.Form):
    name = forms.CharField(max_length=10)
    email = forms.EmailField()
    txt = forms.CharField(widget=forms.Textarea)
