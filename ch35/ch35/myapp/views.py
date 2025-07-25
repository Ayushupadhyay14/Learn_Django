# from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from myapp.models import Student
from django.core.serializers import serialize
# Create your views here.


# def home_view(request):
#     return HttpResponse("<h1>this is a home page</h1>")
# def home_view(request):
#     data = {
#         'massage': "home page",
#         'status': 'success'
#     }
#     return JsonResponse(data)
"""------HERE CHANGE STATUS CODE ------"""


# def home_view(request):
#     data = {
#         'massage': "home page",
#         'status': 'success'
#     }
#     return JsonResponse(data, status=200)

"""HERE RETURN A Queryset data"""
# def home_view(request):
#     data = ['Ayush', 'raj', 'sonam']
#     return JsonResponse(data, safe=False)


def home_view(request):
    data = serialize('json', Student.objects.all())
    return JsonResponse(data, status=200, safe=False)
