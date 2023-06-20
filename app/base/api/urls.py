from django.urls import path

from base import views

app_name = "base_api"

urlpatterns = [
    path("api/v1/import_excel/", views.ImportExcelAPIView.as_view(), name="import_excel"),
]
