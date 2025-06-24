from django.urls import path
from student.views import setcookie, getcookie
urlpatterns = [
    path('set-cookie/', setcookie, name='setcookie'),
    path('getcookie/', getcookie, name='getcookie'),
]
