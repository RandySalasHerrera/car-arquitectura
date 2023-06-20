from coursescraped.utils import get_courses, get_driver
from coursescraped import models
from rest_framework import generics
from rest_framework.response import Response



class CourseScrapedAPIView(generics.ListAPIView):
    URL = "https://edutin.com/cursos-gratis#categories"

    def get(self, request, *args, **kwargs):
        driver = get_driver()
        driver.get(self.URL)
        driver.implicitly_wait(10)

        course_list = get_courses(driver)

        for course_name in course_list:
            if not models.CursoScraped.objects.filter(name=course_name).exists():
                models.CursoScraped.objects.create(name=course_name)

        data = {
            'status': 200,
            'message': 'datos procesados correctamente',
            'data': course_list
        }
 
        return Response(data=data)
