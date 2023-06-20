from django.db import models

from coursescraped.models import CursoScraped
from student.models import Student
from teacher.models import Teacher

# Create your models here.
class Course(models.Model):
    course_scraped = models.ForeignKey(CursoScraped, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    active = models.BooleanField(default=True)

    def __str__(self):
            return self.course_scraped.name

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        ordering = ['-id']