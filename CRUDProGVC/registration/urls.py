from django.urls import path
from registration import views

urlpatterns = [
    path('profile/', views.ProfileTemplateView.as_view(), name='profile')
]
