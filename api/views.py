from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from rest_framework import generics
from rest_framework import mixins
from .serializers import AcademicSerializer, CitationSerializer, KeywordSerializer, UniversitySerializer, DepartmentSerializer
from .models import Academic, Citation, Keyword, University, Department

# Create your views here.

def home(request):
    return render(request, 'api/home.html')

class AcademicListAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    queryset = Academic.objects.all()
    serializer_class = AcademicSerializer

    def perform_create(self, serializer):
        serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CitationListAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    queryset = Citation.objects.all()
    serializer_class = CitationSerializer

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

