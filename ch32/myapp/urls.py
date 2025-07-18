from django.urls import path
from myapp import views
from myapp.views import StudentimageView


urlpatterns = [
    path('<int:pk>/', views.SingleStudentView.as_view(),
         name='single_students'),
    path('student/<int:pk>/', views.StudentDetailView.as_view(),
         name='studentdetail'),

    path('student/<int:pk>/', StudentimageView.as_view(), name='student_detail'),
]
