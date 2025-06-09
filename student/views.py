from django.shortcuts import render
from student.forms import Registration  # This should be your form class
from django.http import HttpResponseRedirect
from student.models import Profile


def registration_view(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            pw = form.cleaned_data['password']
            # print("Name:", name)
            # print("Email:", email)
            # print("Password:", password)

            # save data in data base first create a model:
            user = Profile(name=nm, email=em, password=pw)
            user.save()
            return HttpResponseRedirect('/student/Registration/')
    else:
        form = Registration()  # This must be assigned even when GET method

    return render(request, 'student/index.html', {'form': form})
