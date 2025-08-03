from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import FormView
from myapp.forms import ContactForm
from .models import Contact

# Create your views here.


class ContactFormView(FormView):

    template_name = 'myapp/contact.html'
    form_class = ContactForm

    def form_valid(self, form):
        print(form.cleaned_data['name'])
        print(form.cleaned_data['email'])
        print(form.cleaned_data['msg'])

        return HttpResponse('thank You form submitted')
