import django_filters
from .models import Blogs



class BlogFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title',lookup_expr='icontains')
    content = django_filters.CharFilter(field_name='content',lookup_expr='icontains')
    
    
    class Meta:
        model = Blogs
        fields = ['title', 'content']