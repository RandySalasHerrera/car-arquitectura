from django.contrib import admin

from coursescraped import models

# from coursescraped import models

# Register your models here.
@admin.register(models.CursoScraped)
class CursoScraped(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ['name']
    ordering = ("name",)
    icon_name = "import_contacts"

