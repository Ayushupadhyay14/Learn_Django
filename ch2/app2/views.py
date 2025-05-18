from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# def home(request):
#     return HttpResponse('<h1>home page app2 data <h1\>')

def app1(request):
    return HttpResponse('<h1>home page 1 app 2 data<h1\>')
