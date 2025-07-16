from django.contrib import admin
from myapp.models import Profile
# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "Email", "city"]
