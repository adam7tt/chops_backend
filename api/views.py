from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import mixins
from .serializers import AcademicSerializer, CitationSerializer, KeywordSerializer, UniversitySerializer, DepartmentSerializer
from .models import *
from .filters import *

# Create your views here.

def home(request):
    return render(request, 'api/home.html')

class AcademicListAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = AcademicSerializer
    queryset = Academic.objects.all()
    filter_class = AcademicFilter
    filter_backends = [DjangoFilterBackend]

    def perform_create(self, serializer):
        serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CitationListAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    queryset = Citation.objects.all()
    serializer_class = CitationSerializer
    filter_class = CitationFilter
    filter_backends = [DjangoFilterBackend]

    def perform_create(self, serializer):
        serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class KeywordListAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer

    def perform_create(self, serializer):
        serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class UniversityListAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

    def perform_create(self, serializer):
        serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class DepartmentListAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def perform_create(self, serializer):
        serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

