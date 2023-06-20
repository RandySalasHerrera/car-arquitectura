from django.contrib import admin

from course import models

# Register your models here.
@admin.register(models.Course)
class CursoScraped(admin.ModelAdmin):
    list_display = ("course_scraped","teacher",)
    search_fields = ['course_scraped']
    ordering = ("-id",)
    icon_name = "import_contacts"