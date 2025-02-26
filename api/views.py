from student.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET'])
def students_view(request):
    if request.method == 'GET':
        # Get all the data from the Student table
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        # Why 'many=True' because the students returns data of differents types and we need if for tratament
        return Response(serializer.data, status=status.HTTP_200_OK)
