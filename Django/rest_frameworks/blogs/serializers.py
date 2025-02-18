from rest_framework import serializers
from .models import Blogs, Comments



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'
    
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = '__all__'
    comments = CommentSerializer(many=True, read_only=True)
    