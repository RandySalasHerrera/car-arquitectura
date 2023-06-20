from django.db import models

# Create your models here.
class ExcelFileUpload(models.Model):

    file = models.FileField(upload_to="excel")
