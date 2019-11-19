from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, mixins, filters
from .serializers import AcademicSerializer, CitationSerializer, KeywordSerializer, UniversitySerializer, DepartmentSerializer
from .models import *
from .filters import *

def home(request):
    return render(request, 'api/home.html')

class AcademicListAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = AcademicSerializer
    queryset = Academic.objects.all()
    filter_class = AcademicFilter
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name', 'university__name', 'department__name', 'citations__keywords__name']
    
    def perform_create(self, serializer):
        serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CitationListAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    queryset = Citation.objects.all()
    serializer_class = CitationSerializer
    filter_class = CitationFilter
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title', 'date', 'keywords__name']

    def perform_create(self, serializer):
        serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class KeywordListAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']

    def perform_create(self, serializer):
        serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class UniversityListAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']

    def perform_create(self, serializer):
        serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class DepartmentListAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']

    def perform_create(self, serializer):
        serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

