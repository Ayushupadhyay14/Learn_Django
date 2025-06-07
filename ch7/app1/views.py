from django.shortcuts import render

# Create your views here.


def cafe_home(req):
    return render(req, 'app1/cafe_home.html')


def About_Cafe(req):
    return render(req, 'app1/About.html')
