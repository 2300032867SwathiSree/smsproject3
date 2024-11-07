from django.db import models

# Create your models here.
from adminapp.models import StudentList


class AddCourse(models.Model):
    COURSE_CHOICES = [
        ('AOOP', 'Advanced Object-Oriented Programming'),
        ('PFSD', 'Python Full Stack Development'),

    ]
    SECTION_CHOICES = [
        ('s11', 'Section s11'),
        ('s12', 'Section s12'),
        ('s13', 'Section s13'),
        ('s14', 'Section s14'),
        ('s15', 'Section s15'),
    ]
    student = models.ForeignKey(StudentList, on_delete=models.CASCADE)
    course = models.CharField(max_length=50, choices=COURSE_CHOICES)
    section = models.CharField(max_length=50, choices=SECTION_CHOICES)

    def _str_(self):
        return f'{self.student.Register_Number} - {self.course} ({self.section})'

class Marks(models.Model):
    COURSE_CHOICES = [
        ('AOOP', 'Advanced Object-Oriented Programming'),
        ('PFSD', 'Python Full Stack Development'),
    ]

    student = models.ForeignKey(StudentList, on_delete=models.CASCADE)
    course = models.CharField(max_length=50, choices=COURSE_CHOICES)
    marks = models.IntegerField()
    def __str__(self):
        return f"{self.student.name} - {self.course}"