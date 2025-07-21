
from django.urls import path
from myapp import views

urlpatterns = [
    path('create/', views.StudentCreateView.as_view(), name='create'),
]
