from django.shortcuts import render
from datetime import datetime

# from django.http import HttpResponse
# Create your views here.


def learn_Django(req):
    # here name, of a Template Engine and File Name of a htlm :
    # coursename = {'cname': 'Python'}
    d = datetime.now()
    return render(req, 'course/django.html', context={'dt': d}, status=200)


def Show_data(req):
    return render(req, 'course/fastapi.html', status=200)
