from django.shortcuts import render
from django.db.models import Count, Sum, Avg, F
from .models import Author, Book
# Create your views here.


def home(request):
    # here Count the number og book each auther has
    authors = Author.objects.select_related('author').all()
    # author = Author.objects.update(id=1)
    print(authors)
    # print(vars(authors[1]))
    for author in authors:
        print(author.id, author.name)
    # print(authors)
    # print(authors.values('id'))
    return render(request, 'app/index.html')
