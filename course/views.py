from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.


def learn_Django(req):
    # here name, of a Template Engine and File Name of a htlm :
    return render(req, 'course/django.html', status=200)


def Show_data(req):
    return render(req, 'course/fastapi.html',status=200)
