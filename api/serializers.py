from rest_framework import serializers
from .models import *

class AcademicSerializer(serializers.ModelSerializer):
    university = serializers.SlugRelatedField(
        slug_field='name',
        many=False,
        read_only=True
     )
    department = serializers.SlugRelatedField(
        slug_field='name',
        many=False,
        read_only=True
     )
    citations = serializers.SlugRelatedField(
        slug_field='title',
        many=True,
        read_only=True
     )
    class Meta:
        model = Academic
        fields = "__all__"

class CitationSerializer(serializers.ModelSerializer):
    keywords = serializers.SlugRelatedField(
        slug_field='name',
        many=True,
        read_only=True
     )
    class Meta:
        model = Citation
        fields = "__all__"

class KeywordSerializer(serializers.ModelSerializer):

     class Meta:
        model = Keyword
        fields = "__all__"

class UniversitySerializer(serializers.ModelSerializer):

    class Meta:
        model = University
        fields = "__all__"

class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = "__all__"

# class SchoolsSerializer(serializers.ModelSerializer):
#
#
#     class Meta:
#
#         model = Schools
#         fields = ('name')
#
