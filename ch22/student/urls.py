from django.urls import path
from student.views import home
from student.views import user_info
from student.views import my_math


urlpatterns = [
    path('', home, name='home'),
    path('math/', my_math, name='my_math'),
    path('info/', user_info, name='user_info'),
]
