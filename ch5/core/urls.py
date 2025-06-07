from django.urls import path
from core.views import learn_python
from core.views import show1

urlpatterns = [
    path('py/', learn_python),
    path('c/', show1),
]
