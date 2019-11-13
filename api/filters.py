import django_filters
from .models import *

class AcademicFilter(django_filters.FilterSet):

    professor = django_filters.CharFilter('name', lookup_expr='iexact')
    university = django_filters.CharFilter('university__name', lookup_expr='iexact')
    department = django_filters.CharFilter('department__name', lookup_expr='iexact')
    keywords = django_filters.ModelMultipleChoiceFilter('citations__keywords__name', lookup_expr='iexact',
            queryset=Keyword.objects.all(), conjoined=True)

    class Meta:
        model = Academic
        filters = ()
        exclude = ()


class CitationFilter(django_filters.FilterSet):

    title = django_filters.CharFilter('title', lookup_expr='icontains')
    year = django_filters.NumberFilter(field_name='date', lookup_expr='year')
    keywords = django_filters.ModelMultipleChoiceFilter('keywords__name', lookup_expr='iexact',
            queryset=Keyword.objects.all(), conjoined=True)

    class Meta:
        model = Citation
        filters = ()
        exclude = ()

