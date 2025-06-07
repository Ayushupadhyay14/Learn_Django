from django.urls import path
from student.views import Registration
urlpatterns = [
    path('Registration/', Registration, name='Registration'),
]
