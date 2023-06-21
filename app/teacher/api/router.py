from teacher.api.views import TeacherViewSet
from rest_framework.routers import DefaultRouter

router_teacher = DefaultRouter()

router_teacher.register(prefix='teacher', basename='teacher', viewset=TeacherViewSet)

