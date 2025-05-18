from django.urls import path, include
from django.urls import path
from app6.views import About,contact as ap6



urlpatterns = [
    path('About/', ap6),
    path('contact/', ap6),
              # same user same data render
]