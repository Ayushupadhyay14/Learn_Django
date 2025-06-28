from django.urls import path
from core.views import home, about, contact, base
urlpatterns = [
    path('', base, name='base'),
    path('about/', about, name='about'),
    path('home/', home, name='home'),
    path('contact/', contact, name='contact'),

]
