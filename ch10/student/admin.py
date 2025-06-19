from django.contrib import admin
from student.models import Profile
# Register your models here.
# admin.site.register(Profile)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'city')


# here register
admin.site.register(Profile, ProfileAdmin)
