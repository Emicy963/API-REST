from rest_framework import serializers
from .models import Blog, Coment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coment
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
