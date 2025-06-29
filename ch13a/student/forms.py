from django.forms import ModelForm
from student.models import Profile
from django import forms
GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)

# JOB_CITY_CHOICE = (
#     ('Indore', 'Indore'),
#     ('Delhi', 'Delhi'),
#     ('Pune', 'Pune'),
#     ('Hydrabad', 'Hydrabad'),
#     ('Bangalore', 'Bangalore'),
# )


class ProfileForm(forms.ModelForm):
    # job_city = forms.CharField(JOB_CITY_CHOICE)
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES, widget=forms.RadioSelect,
    )
    # job_city = forms.MultipleChoiceField(

    #     label="Preferred Job Cities"
    # )

    class Meta:
        model = Profile
        fields = [
            'name', 'dob', 'gender', 'locality', 'city', 'pin', 'state', 'mobile', 'email', 'job_city', 'profile_image', 'my_file']
        fields = '__all__'  # or explicitly list them

        labels = {
            'name': 'Full Name',
            'pin': 'Pin code',
            'mobile': 'Mobile Number',
            'dob': 'Date Of Birth'
        }
        help_texts = {
            'profile_image': 'Optional: Upload a profile image',
            'my_file': 'Optional: Attact any additional document(PDF, DOCX, etc)'
        }
        widgets = {
            'dob': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'id': 'datepicker'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your full name'
            }),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'locality': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Locality'
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'City'
            }),
            'pin': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Pin Code'
            }),
            # 'state': forms.TextInput(attrs={
            #     'class': 'form-select',
            #     'placeholder': 'State'
            # }),
            'mobile': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '10-digit Mobile Number'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'example@email.com'
            }),
            'job_city': forms.Select(attrs={'class': 'form-select'}),
            'profile_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'my_file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
