from django import forms
# from django.core import validators
from .models import Profile
# buils validator in python for a forms filling :


# class Registration(forms.Form):
#     name = forms.CharField(validators=[validators.MaxLengthValidator(
#         15), validators.MinLengthValidator(5)])
#     email = forms.CharField(validators=[validators.EmailValidator()])
#     password = forms.CharField(
#         widget=forms.PasswordInput)

# it is a form API it use to form documation:

# class Registration(forms.Form):
#     name = forms.CharField(
#         error_messages={"required": "Please enter your name"})
#     email = forms.CharField(error_messages={'please': 'email is a required'})
#     password = forms.CharField(
#         error_messages={'please': 'password is a required'}, widget=forms.PasswordInput)

class Registration(forms.ModelForm):
    name = forms.CharField(max_length=50)
    Conform_Password = forms.CharField(widget=forms.PasswordInput())
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Profile
        fields = ['name', 'email', 'password']
        labels = {'name': "Enter a name", 'email': "Enter A emai_id",
                  'password': "Enter A Password"}
        # exclude = ['email']  # This will include all fields except 'email'
        error_massages = {'email': {'required': 'this fiels are required'}}
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'pwdclass'}),
            'name': forms.TextInput(attrs={'class': 'myclass', 'placeholder': 'yaha name likhna hia:'})
        }
