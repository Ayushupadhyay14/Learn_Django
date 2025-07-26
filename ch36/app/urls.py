
from django.urls import path, include
from app.views import home
urlpatterns = [
    path('', home, name='book'),
]
