from django.views.generic import ListView
from .models import Book
from django.views.generic import TemplateView, RedirectView
from django.views import View
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import BookForm  # ✅ CORRECT
from django.views.generic.edit import CreateView


class BookCreateView(View):
    def get(self, request):
        form = BookForm()
        return render(request, 'book/book_form.html', {'form': form})


class BookListView(ListView):
    model = Book
    template_name = 'book/book_list.html'
    context_object_name = 'books'
