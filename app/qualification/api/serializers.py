from qualification.models import Qualification
from rest_framework import serializers


class QualificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Qualification
        fields = ['course', 'student', 'qualification']