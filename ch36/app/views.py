from django.shortcuts import render
from django.db.models import Count, Sum, Avg, F
from .models import Author, Book
# Create your views here.


def home(request):
    # here Count the number og book each auther has
    authors = Author.objects.annotate(Count('book'))
    print(authors)
    print(authors.values('id'))
    return render(request, 'app/index.html')
