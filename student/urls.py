from django.urls import path
from student.views import ExampleForm
urlpatterns = [
    path('app/', ExampleForm, name='ExampleForm'),
]
