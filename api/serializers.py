from rest_framework import serializers
from student.models import Student
from employed.models import Employed

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class EmployedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employed
        fields = '__all__'
