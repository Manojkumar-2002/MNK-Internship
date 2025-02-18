
from .models import Blogs, Comments
from .serializers import BlogSerializer, CommentSerializer
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .filter import BlogFilter




# Create your views here.

class Blog(viewsets.ModelViewSet):
    queryset = Blogs.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BlogFilter
    
    
class Comment(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
