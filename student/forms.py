from django import forms


class ExampleForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    # dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    # agree = forms.BooleanField(required=True)
    # gender = forms.ChoiceField(
    #     choices=[('M', 'Male'), ('F', 'Female')], widget=forms.RadioSelect)
    # document = forms.FileField()
    # FileField = forms.FileField()
