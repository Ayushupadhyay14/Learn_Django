from django.contrib import admin
from student.models import Profile
from student.forms import ProfileForm


class ProfileAdmin(admin.ModelAdmin):
    form = ProfileForm
    list_display = [
        'name', 'dob', 'gender', 'locality', 'city', 'pin', 'state',
        'mobile', 'email', 'job_city', 'profile_image', 'my_file'
    ]


admin.site.register(Profile, ProfileAdmin)
