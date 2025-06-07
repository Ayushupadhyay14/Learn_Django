from django.urls import path
from app1.views import cafe_home
from app1.views import About_Cafe

urlpatterns = [
    path('home/', cafe_home),
    path('About/', About_Cafe),
]
