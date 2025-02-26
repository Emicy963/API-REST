from django.shortcuts import render
from django.http import JsonResponse

def students_view(request):
    students = {
        'id': 1,
        'name': 'Anderson Cafurica',
        'class': 'Computer Science',
    }
    return JsonResponse(students)
