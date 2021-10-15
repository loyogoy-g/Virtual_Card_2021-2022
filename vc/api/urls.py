from django.urls import path
from . import views

urlpatterns = [
    path('', views.Schoolyear, name='apiSY'),
    path('students', views.student , name='student')
]