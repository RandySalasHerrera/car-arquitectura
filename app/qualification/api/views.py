
from qualification.api.serializers import QualificationSerializer
from qualification.models import Qualification
from rest_framework import viewsets


class QualificationViewSet(viewsets.ModelViewSet):
    queryset = Qualification.objects.all()
    serializer_class = QualificationSerializer

