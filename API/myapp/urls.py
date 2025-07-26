from django.urls import path
from myapp.views import home, ProductApi


# here create urls :
urlpatterns = [
    path('', home, name='home'),
    path('api/product/', ProductApi.as_view(), name='products'),

]
