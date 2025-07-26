from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views import View
from .froms import ProductForm
from .models import Product
# Create your views here.


def home(request):
    return render(request, 'myapp/index.html')


class ProductApi(View):
    def get(self, request):
        products = list(Product.objects.values('id', 'name', 'price'))
        return JsonResponse(products, safe=False)
