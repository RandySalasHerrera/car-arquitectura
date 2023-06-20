import os
from django.conf import settings
from base.utils import createUser, createTeacher
from base import models
from student import models as models_student
from rest_framework import generics
from rest_framework.response import Response
from openpyxl import load_workbook


# Create your views here.
class ImportExcelAPIView(generics.ListAPIView):

    def post(self, request, format=None):
        try:
            excel_upload = models.ExcelFileUpload.objects.create(file=request.FILES["file"])
            filename = f"{settings.APPS_DIR}/config{settings.MEDIA_URL}{excel_upload.file}"

            wb = load_workbook(excel_upload.file)

            nombres_hojas = ['Hoja1', 'Hoja2']
            for nombre_hoja in nombres_hojas:

                hoja = wb[nombre_hoja]

                if nombre_hoja == 'Hoja1':
                    student = createUser(hoja)
                    estudiantes_creados, estudiantes_error = student
                
                if nombre_hoja == 'Hoja2':
                    student = createTeacher(hoja)
                    teacher_creados, teacher_error = student
                
            wb.close()

            if os.path.isfile(filename):
                os.remove(filename)

            data = {
                'status': 200,
                'estudiantes_creados': f'Se crearon {estudiantes_creados} estudiantes correctamente',
                'estudiantes_error': f'Se crearon {estudiantes_error} estudiantes errores',
                'teacher_creados': f'Se crearon {teacher_creados} teacher correctamente',
                'teacher_error': f'Se crearon {teacher_error} teacher errores'
            }

            return Response(data=data)

        except Exception as e:
            data = {
                'status': 500,
                'message': f'Error: {str(e)}'
            }
            return Response(data=data)
