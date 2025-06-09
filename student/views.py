from django.shortcuts import render
from student.forms import ExampleForm

# fm = ExampleForm()
# Create your views here


def ExampleForm(req):
    if req.method == 'POST':
        form = ExampleForm(req.POST)
        print(req.POST['email'])
        print(req.POST['password'])
    else:
        form = ExampleForm()
    return render(req, 'student/all.html', {'form': form})
