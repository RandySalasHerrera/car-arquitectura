from django.db import models

# Create your models here.
class CursoScraped(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Course Scraped"
        verbose_name_plural = "List Course Scrapeds"
        ordering = ['-name']

