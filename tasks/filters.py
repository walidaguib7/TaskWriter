from django_filters import rest_framework as filters
from .models import Tasks

class TaskFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    status = filters.NumberFilter(field_name='status')
    priority = filters.NumberFilter(field_name='priority')

    class Meta:
        model = Tasks
        fields = ['name', 'status', 'priority', 'category']