# from django.shortcuts import render
from myapp.models import Student  # here import studemt models
from django.views.generic import ListView, DateDetailView, CreateView, DeleteView, UpdateView
# HERE INMPORT (GENERIC LIBARY CLSS IMPORT VIEWS)
# Create your views here.


class StudentCreateView(CreateView):
    model = Student
    success_url = '/'
    # Make sure this file exists
