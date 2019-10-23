from rest_framework import serializers
from .models import *


class CitationsSerializer(serializers.ModelSerializer):


    class Meta:

        model = Citations
        fields = ('abstract','collaborators', 'title', 'date', 'paper')
      #  read_only_fields = ('abstract','collaborators', 'title', 'date', 'paper')

# class KeywordsSerializer(serializers.ModelSerializer):
#
#
#     class Meta:
#
#         model = Keywords
#         fields = ('name')
#
# class AcademicsSerializer(serializers.ModelSerializer):
#
#
#     class Meta:
#
#         model = Academics
#         fields = ('name')
#
# class UniversitySerializer(serializers.ModelSerializer):
#
#
#     class Meta:
#
#         model = University
#         fields = ('name')
#
# class SchoolsSerializer(serializers.ModelSerializer):
#
#
#     class Meta:
#
#         model = Schools
#         fields = ('name')
#
# class DepartmentsSerializer(serializers.ModelSerializer):
#
#
#     class Meta:
#
#         model = Departments
#         fields = ('name')
