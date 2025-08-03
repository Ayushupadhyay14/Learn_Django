# from django.contrib import admin
from django.urls import path
from myapp.views import post_list
urlpatterns = [
    path('home/', post_list, name='post'),

]
