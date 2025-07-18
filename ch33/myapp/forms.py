from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Your Name")
    email = forms.EmailField(label="Your Email")
    msg = forms.CharField(label="Your Message", widget=forms.Textarea)
