# from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import JsonResponse

# Create your views here.


# def home_view(request):
#     return HttpResponse("<h1>this is a home page</h1>")
def home_view(request):
    data = {
        'massage': "home page",
        'status': 'success'
    }
    return JsonResponse(data)
