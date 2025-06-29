# from django.db import models
# from django.core.exceptions import ValidationError
# from django.core import validators
# from django.core.validators import RegexValidator

# # create a costume validators


# def validate_pin_length(value):
#     if len(str(value)) != 6:
#         raise ValidationError('the pin code must be Exacty 6 digit')
# # Create your models here.


# STATE_CHOICES = [
#     ('AN', 'Andaman and Nicobar Islands'),
#     ('AP', 'Andhra Pradesh'),
#     ('AR', 'Arunachal Pradesh'),
#     ('AS', 'Assam'),
#     ('BR', 'Bihar'),
#     ('CH', 'Chandigarh'),
#     ('CG', 'Chhattisgarh'),
#     ('DN', 'Dadra and Nagar Haveli and Daman and Diu'),
#     ('DL', 'Delhi'),
#     ('GA', 'Goa'),
#     ('GJ', 'Gujarat'),
#     ('HR', 'Haryana'),
#     ('HP', 'Himachal Pradesh'),
#     ('JK', 'Jammu and Kashmir'),
#     ('JH', 'Jharkhand'),
#     ('KA', 'Karnataka'),
#     ('KL', 'Kerala'),
#     ('LA', 'Ladakh'),
#     ('LD', 'Lakshadweep'),
#     ('MP', 'Madhya Pradesh'),
#     ('MH', 'Maharashtra'),
#     ('MN', 'Manipur'),
#     ('ML', 'Meghalaya'),
#     ('MZ', 'Mizoram'),
#     ('NL', 'Nagaland'),
#     ('OD', 'Odisha'),
#     ('PY', 'Puducherry'),
#     ('PB', 'Punjab'),
#     ('RJ', 'Rajasthan'),
#     ('SK', 'Sikkim'),
#     ('TN', 'Tamil Nadu'),
#     ('TS', 'Telangana'),
#     ('TR', 'Tripura'),
#     ('UP', 'Uttar Pradesh'),
#     ('UK', 'Uttarakhand'),
#     ('WB', 'West Bengal'),
# ]


# class profile(models.Model):
#     name = models.CharField(max_length=100)
#     dob = models.DateField(auto_now=False, auto_now_add=False)
#     age = models.CharField(max_length=100)
#     gender = models.CharField(max_length=1)
#     # mobile_number = models.CharField(max_length=100)
#     locality = models.CharField(max_length=100)
#     city = models.CharField(max_length=100)
#     pin = models.PositiveIntegerField(
#         validators=[validate_pin_length], help_text='Enter 6 digit pin code')
#     state = models.CharField(choices=STATE_CHOICES, max_length=100)
#     mobile = models.CharField(
#         Validators=[RegexValidator(regex=r'^\d{10}$')],
#         max_length=10, help_text='enter 10 digit mobile number:')
#     email = models.EmailField()
#     job_city = models.CharField(max_length=50)
#     profile_image = models.ImageField(upload_to='profileimg', blank=False)
#     my_file = models.FileField(upload_to='doc', blank=True
#                                )

#     def __str__(self):
#         return self.name

from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

# Custom PIN code validator


def validate_pin_length(value):
    if len(str(value)) != 6:
        raise ValidationError('The pin code must be exactly 6 digits')


# Indian states
STATE_CHOICES = [
    ('AN', 'Andaman and Nicobar Islands'),
    ('AP', 'Andhra Pradesh'),
    ('AR', 'Arunachal Pradesh'),
    ('AS', 'Assam'),
    ('BR', 'Bihar'),
    ('CH', 'Chandigarh'),
    ('CG', 'Chhattisgarh'),
    ('DN', 'Dadra and Nagar Haveli and Daman and Diu'),
    ('DL', 'Delhi'),
    ('GA', 'Goa'),
    ('GJ', 'Gujarat'),
    ('HR', 'Haryana'),
    ('HP', 'Himachal Pradesh'),
    ('JK', 'Jammu and Kashmir'),
    ('JH', 'Jharkhand'),
    ('KA', 'Karnataka'),
    ('KL', 'Kerala'),
    ('LA', 'Ladakh'),
    ('LD', 'Lakshadweep'),
    ('MP', 'Madhya Pradesh'),
    ('MH', 'Maharashtra'),
    ('MN', 'Manipur'),
    ('ML', 'Meghalaya'),
    ('MZ', 'Mizoram'),
    ('NL', 'Nagaland'),
    ('OD', 'Odisha'),
    ('PY', 'Puducherry'),
    ('PB', 'Punjab'),
    ('RJ', 'Rajasthan'),
    ('SK', 'Sikkim'),
    ('TN', 'Tamil Nadu'),
    ('TS', 'Telangana'),
    ('TR', 'Tripura'),
    ('UP', 'Uttar Pradesh'),
    ('UK', 'Uttarakhand'),
    ('WB', 'West Bengal'),
]

# Gender choices (optional improvement)
GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
]

# city choihc for a job
JOB_CITY_CHOICE = (
    ('Indore', 'Indore'),
    ('Delhi', 'Delhi'),
    ('Pune', 'Pune'),
    ('Hydrabad', 'Hydrabad'),
    ('Bangalore', 'Bangalore'),
)

# Profile model


class Profile(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin = models.PositiveIntegerField(
        validators=[validate_pin_length],
        help_text='Enter 6 digit pin code'
    )
    state = models.CharField(choices=STATE_CHOICES, max_length=100)
    mobile = models.CharField(
        validators=[RegexValidator(regex=r'^\d{10}$')],
        max_length=10,
        help_text='Enter 10 digit mobile number'
    )
    email = models.EmailField()
    job_city = models.CharField(choices=JOB_CITY_CHOICE, max_length=50)
    profile_image = models.ImageField(upload_to='profileimg', blank=False)
    my_file = models.FileField(upload_to='doc', blank=True)

    # def __str__(self):
    #     return self.name
