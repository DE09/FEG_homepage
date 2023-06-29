from django import forms

class ContactForm(forms.Form):
    
    company = forms.CharField(max_length=255)
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)
    message = forms.CharField(widget=forms.Textarea)
    imex = forms.CharField(max_length=20)
    incoterms = forms.CharField(max_length=20)
    shippingmode = forms.CharField(max_length=20)