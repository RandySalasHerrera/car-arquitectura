from student.api.views import StudentViewSet
from rest_framework.routers import DefaultRouter

router_student = DefaultRouter()

router_student.register(prefix='student', basename='student', viewset=StudentViewSet)

