from django.contrib import admin
from student.models import profile, Result
# Register your models here.

# # admin.site.register(profile)

# here use a decorator in this top line like -(admin.register(profile))
class profileAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll')


admin.site.register(profile, profileAdmin)

# here register a result clasds model to show data


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')
# here also use a decorator to show resulr :
# admin.site.register(Result, ResultAdmin)
