# from django.contrib import admin
from student.views import home  
# , test
from django.urls import path


urlpatterns = [
    path('', home, name='home'),
    # path('home/', test, name='test'),
]
