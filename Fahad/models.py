from django.db import models

class Course(models.Model):
    teacher_name=models.CharField(max_length=30)
    course_name=models.CharField(max_length=30)
    duration=models.IntegerField()
    seat=models.IntegerField()
