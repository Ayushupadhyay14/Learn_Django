from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.ContactFormView.as_view(), name="contact"),
]
