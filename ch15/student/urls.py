from django.urls import path
from student.views import home

urlpatterns = [
    path('', home, name='home'),
]
