from django.shortcuts import render

# Create your views here.


def learn_python(req):
    return render(req, 'core/python.html')


def show1(req):
    return render(req, 'core/core.html')
