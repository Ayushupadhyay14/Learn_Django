from django.shortcuts import render
from student.models import Student  # here import a model of a student
# Create your views here.


def home(request):
    # student_data = Student.objects.get(name="Ayush")# it use to return a name of a database table = "Ayush" you can search and kind of a fields does given a database :

    # to return a first value on the data base table : Id number first top value:
    # student_data = Student.objects.first()
    # student_data = Student.objects.order_by('name').first()
    # student_data = Student.objects.order_by('name').last()
    # student_data = Student.objects.latest('pass_date')
    # student_data = Student.objects.all()
    # if return True so data is exists/ if False not exist
    """CREATE AND GET DATA """
    # student_data, created = Student.objects.get_or_create(
    #     name="Ashis", roll=302, city="indore", marks=70, pass_date='2003-08-13')
    # print(created)

    # print(student_data.exists())
    """UPDATE DATA BASE METHODS"""
#     student_data = Student.objects.filter(id='1').update(name="Ankur upadhyay")
#     student_data = Student.objects.first()

    """USE TO BULK CREATE A DATABASE """
    """obj = [
        Student(name="sahil", roll=321, city="satna",
                marks=50, pass_date='2020-04-07'),
        Student(name="Anil", roll=320, city="satna",
                marks=70, pass_date='2020-04-07'),
        Student(name="Raj", roll=324, city="satna",
                marks=65, pass_date='2020-04-07'),
        Student(name="Anand", roll=381, city="satna",
                marks=73, pass_date='2020-04-07'),
    ]
    student_data = Student.objects.bulk_create(obj)"""

    """<-----HERE BUILK UPDATE DATA ----->"""
    """all_student_data = Student.objects.all()
    for stu in all_student_data:
        stu.city = 'delhi'
    student_data = Student.objects.bulk_update(all_student_data, ['city'])"""

    """<----HERE USE TO INBULK DATA ---->"""
    """student_data = Student.objects.in_bulk([1, 2])
    print(student_data[1].name)
    print(student_data[2].name)"""

    """HERE USE DELETE METHOS TO DELETE A SPECIFIC DATA"""
    """student_data = Student.objects.get(pk=9).delete()"""
#     student_data = Student.objects.all()
    student_data = Student.Ayush.all()
    print("return:", student_data)
    return render(request, 'student/index.html', {'students': student_data})
