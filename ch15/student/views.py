from django.shortcuts import render
from django.contrib import messages
# Create your views here.


def home(request):
    messages.add_message(request, messages.SUCCESS,
                         "Your Program is Run succesfullfy !! ")
    messages.info(request, "this is a info!!")
    messages.warning(request, "this is a warning!!")
    messages.error(request, "this is a error!!")
    messages.debug(request, "this is a debug!!")
    return render(request, 'student/home.html')
