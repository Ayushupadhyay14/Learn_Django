from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, world! This is the home page.")


def app1_home(request):
    return HttpResponse("<h1> Thjis is a Django code:<h/>")


def add(request):
    a = 12
    b = 23
    c = a+b
    return HttpResponse(f"the sum of {a} and {b} is {c}")


def Show(request):
    lang = '<h1>Hello Ayush ji <h/>'
    return HttpResponse(lang)

