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
            print("user name is:", nm)
            print("user email is:", em)
            print("user password is:", pw)

            
            # HERE USE TO A SAVING DATA - > save() method:
            data = Profile(name=nm, email=em, password=pw)
            data.save()

# HERE USE TO UPDATE DATA FOR DATA DATA BASE -> PASS USER ID
            """data = Profile(id=1, name=nm, email=em, password=pw)
            data.save()"""

# HERE USER TO DELETE METHODS
            data = Profile(id=1)
            data.delete()
            return HttpResponseRedirect('/student/Registration/')
    else:
        form = Registration()  # This must be assigned even when GET method

    return render(request, 'student/index.html', {'form': form})
