from django.shortcuts import render
from django.core.cache import cache
# Create your views here.


# def show(request):
#     mv = cache.get('movie', 'has_expired')
#     if mv == 'has_expired':
#         cache.set('movie', 'the man', 60)
#         mv = cache.get('movie')
#     return render(request, 'student/course.html', {'mv': mv})


"""here use easy way to define """


def course(request):
    mv = cache.get_or_set('movie', 'the man', 60)
    mv1 = cache.get_or_set('movie', 'Ayush Upadhyay', 60, version=2)
    print(mv1)
    return render(request, 'student/course.html', {'mv': mv})
