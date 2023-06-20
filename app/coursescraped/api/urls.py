from django.urls import path

from coursescraped.api import views


app_name = "course_scraped_api"

urlpatterns = [
    path("api/v1/course-scraped/", views.CourseScrapedAPIView.as_view(), name="course_scraped"),
]
