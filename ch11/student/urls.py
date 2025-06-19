from django.urls import path
from student .views import registration_view
# from student .views import Registration_ses
urlpatterns = [
    path('Registration/', registration_view, name="Registration"),
    # path('/', Registration_ses, name="Registration_ses"),
]
