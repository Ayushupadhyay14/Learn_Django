from django.urls import path
from student.views import show

urlpatterns = [
    path('course/', show, name='show'),
]
