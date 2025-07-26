from django.urls import path
from myapp.views import home_view

urlpatterns = [
    path('<int:pk>', home_view, name='home')
]
