from student.models import Student
from employed.models import Employed
from .serializers import StudentSerializer, EmployedSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins, generics

@api_view(['GET', 'POST'])
def students_view(request):
    if request.method == 'GET':
        # Get all the data from the Student table
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        # Why 'many=True' because the students returns data of differents types and we need if for tratament
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def student_detail_view(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

"""class Employees(APIView):
    def get(self, request):
        employess = Employed.objects.all()
        serializer = EmployedSerializer(employess, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, resquest):
        serializer = EmployedSerializer(data=resquest.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class EmployeeDetail(APIView):
    def get_object(self, pk):
        try:
            return Employed.objects.get(pk=pk)
        except Employed.DoesNotExist:
            raise Http404
        
    def get(self, request ,pk):
        employed = self.get_object(pk)
        serializer = EmployedSerializer(employed)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        employed = self.get_object(pk)
        serializer = EmployedSerializer(employed, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)    
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        employed = self.get_object(pk)
        employed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    """    

class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Employed.objects.all()
    serializer_class = EmployedSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class EmployeeDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Employed.objects.all()
    serializer_class = EmployedSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)
        