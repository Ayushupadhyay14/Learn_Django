from django.urls import path
from myapp.views import home, sync_view, asyns_view

urlpatterns = [
    path('', home, name='home'),
    path('sync/', sync_view, name='sync_view'),
    path('aync/', asyns_view, name='asyns_view'),
]
