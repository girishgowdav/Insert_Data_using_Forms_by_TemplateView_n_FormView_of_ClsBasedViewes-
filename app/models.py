from django.db import models

# Create your models here.
class Student(models.Model):
    student_name=models.CharField(max_length=100,primary_key=True)
    age=models.IntegerField()
    course=models.CharField(max_length=100)