import django_filters
from .models import *

class AcademicFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(field_name='id', lookup_expr='iexact')
    name = django_filters.CharFilter('name', lookup_expr='icontains')
    professor = django_filters.CharFilter('name', lookup_expr='iexact')
    university = django_filters.CharFilter('university__name', lookup_expr='icontains')
    department = django_filters.CharFilter('department__name', lookup_expr='icontains')
    keywords = django_filters.CharFilter('citations__keywords__name', lookup_expr='icontains')

    class Meta:
        model = Academic
        filters = ()
        exclude = ()


class CitationFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(field_name='id', lookup_expr='iexact')
    date__gt = django_filters.DateFilter(field_name='date', lookup_expr='gt')
    date__lt = django_filters.DateFilter(field_name='date', lookup_expr='lt')
    title = django_filters.CharFilter('title', lookup_expr='icontains')
    year = django_filters.NumberFilter(field_name='date', lookup_expr='year')
    keyword = django_filters.CharFilter('keywords__name', lookup_expr='icontains')
    keyword_id = django_filters.CharFilter('keywords__id', lookup_expr='iexact')
    professor = django_filters.CharFilter('academic__name', lookup_expr='iexact')

    class Meta:
        model = Citation
        filters = ()
        exclude = ()
