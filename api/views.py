from django.shortcuts import render
from django.http import JsonResponse
from student.models import Student

def students_view(request):
    """ Thats function call the Students atributes and serializers him manually """
    """ Serializer is take the complex data and converter or simplify for a simple data for 'JSON' or 'XML'."""
    students = Student.objects.all()
    students_list = list(students.values())
    return JsonResponse(students_list, safe=False)
