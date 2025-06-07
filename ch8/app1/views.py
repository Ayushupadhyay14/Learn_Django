from django.shortcuts import render
from app1.models import Musician
# Create your views here.


def all_data(req):
    data = Musician.objects.all() # here return a questy set quary set me all object rahta hia 
    return render(req, 'app1/all.html', {'app1': data})
