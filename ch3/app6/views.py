from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def About(request):
    return HttpResponse("<h1>this Aboutus  page<h/>")


def contact(request):
    return HttpResponse('<h1> Welcome to Hellow World<h1/>')
