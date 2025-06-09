from django import forms
# from django.core import validators

# buils validator in python for a forms filling :


# class Registration(forms.Form):
#     name = forms.CharField(validators=[validators.MaxLengthValidator(
#         15), validators.MinLengthValidator(5)])
#     email = forms.CharField(validators=[validators.EmailValidator()])
#     password = forms.CharField(
#         widget=forms.PasswordInput)
class Registration(forms.Form):
    name = forms.CharField(
        error_messages={"required": "Please enter your name"})
    email = forms.CharField(error_messages={'please': 'email is a required'})
    password = forms.CharField(
        error_messages={'please': 'password is a required'}, widget=forms.PasswordInput)
