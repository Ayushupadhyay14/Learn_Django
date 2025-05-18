from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def ap1(request):
    return HttpResponse('<h1> this is A app1 <h/>')
