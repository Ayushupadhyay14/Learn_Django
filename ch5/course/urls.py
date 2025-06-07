from django.urls import path
from course.views import home
from course.views import base
from course.views import django
urlpatterns = [
    path('', home),
    path('b/', base),
    path('d/', django),
]
