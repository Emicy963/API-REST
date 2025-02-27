from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.students_view),
    path('students/<int:pk>', views.student_detail_view),
    #Employed urls
    path('employees/', views.Employees.as_view())
]
