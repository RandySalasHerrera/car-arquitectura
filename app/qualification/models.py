from django.db import models

from course.models import Course
from student.models import Student

# Create your models here.
class Qualification(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    qualification = models.IntegerField()
    active = models.BooleanField(default=True)


    def __str__(self):
            return self.course

    class Meta:
        verbose_name = "Course Scraped"
        verbose_name_plural = "Course Scrapeds"
        ordering = ['-id']