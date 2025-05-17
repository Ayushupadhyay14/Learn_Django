from django.urls import path
from course.views import learn_Django,Show_data

urlpatterns = [
    path('Show/', Show_data),
    path('y/', learn_Django),
]
