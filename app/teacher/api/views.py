
from teacher.api.serializers import TeacherSerializer
from teacher.models import Teacher
from rest_framework import viewsets


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

