from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10, null=True)
    age = models.IntegerField(null=True)
    address = models.CharField(max_length=200,null=True)
    email = models.EmailField(null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
        ordering = ['-name']
