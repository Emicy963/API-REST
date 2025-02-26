from django.shortcuts import render
from django.http import JsonResponse
from student.models import Student

def students_view(request):
    students = Student.objects.all()
    students_list = list(students.values())
    return JsonResponse(students_list, safe=False)
