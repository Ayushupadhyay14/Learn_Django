from django.shortcuts import render, redirect
# inform models from in forms.py file:
from student.forms import ProfileForm
from student.models import Profile
# Create your views here.


def home(request):
    if request == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
           form.save()
           return redirect('home')

    else:
        form = ProfileForm()
    return render(request, 'student/home.html', {'form': form})


# def test(request):
#     return render(request, 'student/home.html', )
