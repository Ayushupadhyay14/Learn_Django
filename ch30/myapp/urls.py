from django.urls import path
from myapp.views import show
urlpatterns = [
    path('', show, name='show'),

]
