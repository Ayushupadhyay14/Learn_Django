from django.urls import path
from django.views.generic.base import TemplateView
urlpatterns = [
    path('index/', TemplateView.as_view(template_name='myapp/index.html'), name='index'),
]
