from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from rest_framework import generics
from .serializers import CitationsSerializer
from .models import Citations

# Create your views here.

def home(request):
    ''
    return render(request, 'api/home.html')

# @staff_member_required
class CreateView(generics.ListCreateAPIView):
    queryset = Citations.objects.all()
    serializer_class = CitationsSerializer

    def perform_create(self, serializer):
        serializer.save()
