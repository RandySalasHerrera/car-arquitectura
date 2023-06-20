from rest_framework_simplejwt.views import TokenObtainPairView
from base.api.serializers import CustomTokenObtainPairSerializer
import os
from django.conf import settings
from base.utils import createUser, createTeacher, createCourse, createQualification
from base import models
from rest_framework import generics
from rest_framework.response import Response
from openpyxl import load_workbook

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class ImportExcelAPIView(generics.ListAPIView):

    def post(self, request, format=None):
        try:
            excel_upload = models.ExcelFileUpload.objects.create(file=request.FILES["file"])
            filename = f"{settings.APPS_DIR}/config{settings.MEDIA_URL}{excel_upload.file}"

            wb = load_workbook(excel_upload.file)

            nombres_hojas = ['Hoja1', 'Hoja2', 'Hoja3', 'Hoja4']
            for nombre_hoja in nombres_hojas:

                hoja = wb[nombre_hoja]

                if nombre_hoja == 'Hoja1':
                    try:
                        student = createUser(hoja)
                        estudiantes_creados, estudiantes_error = student
                    except:
                        pass
                
                if nombre_hoja == 'Hoja2':
                    try:
                        student = createTeacher(hoja)
                        teacher_creados, teacher_error = student
                    except:
                        pass

                if nombre_hoja == 'Hoja3':
                    try:
                        course = createCourse(hoja)
                       # course_creados, course_error = course
                    except:
                        pass
                
                if nombre_hoja == 'Hoja4':
                    try:
                        course = createQualification(hoja)
                       # course_creados, course_error = course
                    except:
                        pass
                
            wb.close()

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
