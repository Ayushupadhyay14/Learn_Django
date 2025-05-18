from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def app2(request):
    return HttpResponse("<h1> this is a app2<h/>")


def app2_me(request):
    return HttpResponse("<h1> this is a app2 hahi<h/>")
