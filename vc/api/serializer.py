from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import SchoolYear, Student, Section, Subject, Quarter

class SchoolYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolYear
        fields = '__all__' 

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__' 