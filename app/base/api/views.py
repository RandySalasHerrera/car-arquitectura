from base.tasks import importFileTask
from rest_framework_simplejwt.views import TokenObtainPairView
from base.api.serializers import CustomTokenObtainPairSerializer
import os
from django.conf import settings
from base import models
from rest_framework import generics
from rest_framework.response import Response


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class ImportExcelAPIView(generics.ListAPIView):

    def post(self, request, format=None):
        try:
            excel_upload = models.ExcelFileUpload.objects.create(file=request.FILES["file"])
            filename = f"{settings.APPS_DIR}/config{settings.MEDIA_URL}{excel_upload.file}"

            importFileTask(excel_upload)

            if os.path.isfile(filename):
                os.remove(filename)

            data = {
                'status': 200,
            }

            return Response(data=data)

        except Exception as e:
            data = {
                'status': 500,
                'message': f'Error: {str(e)}'
            }
            return Response(data=data)
