from django.urls import path, include
from app2.views import app2
from app2.views import home

# Direct Function imaport here


urlpatterns = [
    path('main/', app2),
    path('demo/', app2),
    path('y/',app2), # same user same data render
]
