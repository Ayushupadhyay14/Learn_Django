from django.shortcuts import render

# Create your views here.


def home(req):
    return render(req, 'course/home.html')


def django(req):
    return render(req, 'course/django.html')


def base(req):
    return render(req, 'course/base.html')
