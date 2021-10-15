from django.core import validators
from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.enums import Choices

# Create your models here.

def year_choices():
    return [(r,r) for r in range(1984, datetime.date.today().year+3)]

def current_year():
    return datetime.date.today().year

class SchoolYear(models.Model):
    from_sy = models.IntegerField(verbose_name="From", choices=year_choices() , default=current_year())
    to_sy = models.IntegerField(verbose_name="TO", choices=year_choices(), default=current_year() + 1)
    
    class Meta:
        verbose_name_plural = "1. School Year"

    def __str__(self):
        return f"{self.from_sy} to {self.to_sy}"

class Section(models.Model):
    adviser = models.CharField(max_length=100)
    grade_level = models.IntegerField(default=7, validators=[MinValueValidator(7), MaxValueValidator(12)])
    section = models.CharField(max_length=100)
    sy = models.ForeignKey(SchoolYear, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "3. Section"

    def __str__(self):
        return "{} - {}".format(self.grade_level, self.section)

class Student(models.Model):
    name = models.CharField(max_length=100, unique=True)
    student_id = models.CharField(max_length=100, unique=True)
    lrn = models.CharField(max_length=100, unique=True)
    status = models.BooleanField(verbose_name="Block Access", default=False)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='sections')
    class Meta:
        verbose_name_plural = "2. Students"

    def __str__(self):
        return self.name

class Quarter(models.Model):
    choices = [("First Quarter", "1st Quarter"), ("Second Quarter", "2nd Quarter"), ("Third Quarter", "3rd Quarter"), ("Fourth Quarter", "4th Quarter")]
    quarter = models.CharField(max_length=100, choices=choices)
    
    class Meta:
        verbose_name_plural = "5. Quarter"

    def __str__(self):
        return self.quarter

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)
    grade = models.DecimalField(max_digits=5, decimal_places=2)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    quarter = models.ForeignKey(Quarter, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "4. Subject"

    def __str__(self):
        return self.name




