from django.urls import path
from fees.views import fees
from fees.views import Bca


urlpatterns = [
    path('Fee/', fees),
    path('fees1/', Bca),
]
