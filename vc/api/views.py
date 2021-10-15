from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import SchoolYear, Student, Section, Subject, Quarter
from .serializer import SchoolYearSerializer, StudentSerializer
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def Schoolyear(request):
	tasks = SchoolYear.objects.all()
	serializer = SchoolYearSerializer(tasks, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def student(request):
	tasks = Student.objects.all()
	serializer = StudentSerializer(tasks, many=True)
	return Response(serializer.data)