from django.shortcuts import render

# Create your views here.


def fees(req):

    return render(req, 'fees/Btech.html', status=200)


def Bca(req):
    return render(req, 'fees/Bcafees.html', status=200)
