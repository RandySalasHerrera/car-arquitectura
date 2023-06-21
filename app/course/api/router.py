from course.api.views import CourseViewSet
from rest_framework.routers import DefaultRouter

router_course = DefaultRouter()

router_course.register(prefix='course', basename='course', viewset=CourseViewSet)

