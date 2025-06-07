from django.shortcuts import render
from student.forms import Registration
# Create your views here.

fm = Registration()
def Registration(req):
    return render(req, 'student/Registration.html', {'form': fm})
