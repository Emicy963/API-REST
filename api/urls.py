from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees', views.EmployeesViewset, basename='employee')

urlpatterns = [
    path('students/', views.students_view),
    path('students/<int:pk>', views.student_detail_view),
    #Employed urls
    #path('employees/', views.Employees.as_view()),
    #path('employees/<int:pk>', views.EmployeeDetail.as_view()),

    # Blogs API
    path('', include(router.urls)),
    path('blogs/', views.BlogsView.as_view()),
    path('comments/', views.CommentsView.as_view()),

    path('blogs/<int:pk>', views.BlogDetailView.as_view()),
    path('comments/<int:pk>', views.CommentDetailview.as_view()),
]
