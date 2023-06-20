from django.contrib import admin

from student import models


# Register your models here.
@admin.register(models.Student)
class Student(admin.ModelAdmin):
    list_display = ("name","sex","age")
    search_fields = ['name']
    ordering = ("name",)
    icon_name = "import_contacts"

# Register your models here.
