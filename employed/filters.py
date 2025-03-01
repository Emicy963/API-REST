import django_filters
from .models import Employed

class EmployeeFilter(django_filters.FilterSet):
    designation = django_filters.CharFilter(field_name='designation', lookup_expr='iexact')

    class Meta:
        model = Employed
        fields = ['designation']
