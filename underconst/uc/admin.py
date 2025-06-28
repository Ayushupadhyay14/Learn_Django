from django.contrib import admin
from .models import UnderConstruction
# Register your models here.
# @admin.register(UnderConstruction)
admin.site.register(UnderConstruction)


class UnderConstructionAdmin(admin.ModelAdmin):
    model=UnderConstruction
    list_display = ('id', 'uc_note', 'uc_duration', 'is_under_construction')
    fields = ('uc_note', 'uc_duration', "is_under_construction")
    