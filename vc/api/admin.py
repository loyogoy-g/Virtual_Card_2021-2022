from django.contrib import admin
from django.db import models
from .models import SchoolYear, Student, Section, Subject, Quarter
# Register your models here.


class SubjectInline(admin.TabularInline):
    model = Subject
    extra = 5

class SectionInline(admin.TabularInline):
    model = Section
    extra = 5

@admin.register(SchoolYear)
class SchoolYearAdmin(admin.ModelAdmin):
    inlines = [SectionInline]
    

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "lrn", "status", 'section')
    inlines = [SubjectInline]
    list_filter = ('status', 'section', 'name')