from django.db import models

# Create your models here.
class Department(models.Model):
    dept_name = models.CharField(max_length=30)

class StudentId(models.Model):
    student_id = models.CharField(max_length=10)

class Student(models.Model):
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    s_id = models.OneToOneField(StudentId, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    age = models.IntegerField(max_length=50)
    email = models.CharField(max_length=50)

class Subject(models.Model):
    subject_name = models.CharField(max_length=30)

class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()