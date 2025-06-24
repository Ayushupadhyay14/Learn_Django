from django.shortcuts import render
from datetime import datetime, timedelta, timezone
# Create your views here.


def setcookie(request):

    response = render(request, 'student/setcookie.html')
    response.set_cookie('token', 't12323')  # Basic cookie
    return response

def getcookie(request):
    # token = request.COOKIES['token']
    # token = request.COOKIES.get('token')
    token = request.COOKIES.get('token', 'default_values 123435', expires=datetime.now(
        timezone.utc)+timedelta(days=22))
    return render(request, 'student/getcookie.html', {'token': token})


# def setscookie(request):
#     return render(request, 'student/setsignrdcookie.html')


# def getscookie(request):
#     return render(request, 'student/getsignedcookie.html')
