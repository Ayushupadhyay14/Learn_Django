from django import forms


class Registration(forms.Form):
    first_name = forms.CharField(label="Your Name", max_length=100)
    last_name = forms.CharField(label="Your Name", max_length=100)
    email = forms.EmailField(label="Your Email")
    city = forms.CharField(label="City", widget=forms.Textarea)
