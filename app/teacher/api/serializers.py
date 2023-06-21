from teacher.models import Teacher
from rest_framework import serializers


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = ['name', 'sex', 'age', 'address', 'email']