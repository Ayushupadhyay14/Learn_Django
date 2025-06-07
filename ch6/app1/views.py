from django.shortcuts import render
# Create your views here.


def learn_python(req, **kwargs):
    status = kwargs.get('status')
    return render(req, 'app1/index.html')
