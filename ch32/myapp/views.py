from django.shortcuts import render
from django.views import View
from myapp.models import Student
from django.views.generic.detail import DetailView
# Create your views here.


class SingleStudentView(View):
    def get(self, request, pk):
        single_student = Student.objects.get(pk=pk)
        return render(request, 'myapp/single_student.html',
                      {'single_student': single_student})


class StudentDetailView(DetailView):
    model = Student

class StudentimageView(DetailView):
    model = Student
    template_name = 'myapp/student_detail.html'  # or your correct template name
    context_object_name = 'student'
