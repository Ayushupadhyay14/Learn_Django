from django.shortcuts import render

# Create your views here.


def home(request):
    context = {
        'data': 'hello my name is a Ayuah upadhyay and i am from indore mp madhya pradesh'}
    return render(request, 'student/index.html', context)
