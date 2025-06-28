from django.urls import path
from student.views import course
urlpatterns = [
    path('course/', course, name='course'),
]
