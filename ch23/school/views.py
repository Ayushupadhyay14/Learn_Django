from django.shortcuts import render
from school.models import Student
from django.db.models import QuerySet
# Create your views here.


def home(request):
    # here use all method to retrive all #data for a Student model
    # all_data = Student.objects.all()
    # here get a all data for a city indore in this fiels:
    # all_data = Student.objects.filter(city="indore")

    # give a data do consider indore jo jo indore se nahi hai uska data show hoga
    # all_data = Student.objects.exclude(city="indore")
    # retrive a data from a database in a Order_by on a marks fields data
    # all_data = Student.objects.order_by('marks')
    # here show a random data in a table to exachange data for a data base :
    # all_data = Student.objects.order_by('?')
    # it use to return a data in a Dictonay formate:
    all_data = Student.objects.values()
    # enter a values which data are return or print to a terminal here use to
    # all_data = Student.objects.values('id', 'name')
    # use to values set resturn a values_list() return data in a tuple formate:
    all_data = Student.objects.values_list('name', 'id', named=True)
    print(type(all_data))
    print("all Data", all_data)
    print()
    print("SQL Query:", all_data.query)  # here rutun all sql data Query set
    return render(request, 'school/home.html', {'all_data': all_data})
