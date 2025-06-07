from django.urls import path
from app1.views import learn_python


urlpatterns = [
    path('', learn_python),
]
