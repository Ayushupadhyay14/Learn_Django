from django.shortcuts import render
from django.template.response import TemplateResponse
# Create your views here.


def home(request):
    print("i am home view :")
    return render(request, 'student/home.html')


def my_math(request):
    print("I am my_math View ")
    a = 12/3
    return render(request, 'student/math.html', {'a': a})


def user_info(request):
    print("I am user info view:")
    context = {'name': 'Ayush'}
    return render(request, 'student/index.html', context)
