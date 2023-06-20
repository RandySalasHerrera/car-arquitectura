from django.contrib import admin

from teacher import models

# Register your models here.
@admin.register(models.Teacher)
class Teacher(admin.ModelAdmin):
    list_display = ("name","sex","age")
    search_fields = ['name']
    ordering = ("name",)
    icon_name = "import_contacts"