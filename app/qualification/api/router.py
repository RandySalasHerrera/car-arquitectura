from qualification.api.views import QualificationViewSet
from rest_framework.routers import DefaultRouter

router_qualification = DefaultRouter()

router_qualification.register(prefix='qualification', basename='qualification', viewset=QualificationViewSet)

