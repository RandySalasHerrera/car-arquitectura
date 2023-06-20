from django.contrib import admin

from qualification import models

# Register your models here.
# Register your models here.
@admin.register(models.Qualification)
class Qualification(admin.ModelAdmin):
    list_display = ("course","student","qualification",)
    search_fields = ['course']
    ordering = ("-id",)
    icon_name = "import_contacts"