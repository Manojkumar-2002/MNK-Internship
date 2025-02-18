import django_filters
from .models import Employees



class EmployeeFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name',lookup_expr='icontains')
    branch = django_filters.CharFilter(field_name='branch',lookup_expr='icontains')
    userid = django_filters.RangeFilter(field_name='id')
    
    class Meta:
        model = Employees
        fields = ['name', 'branch','id']