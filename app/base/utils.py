from coursescraped import models as models_course_scraped
from student import models as models_student
from teacher import models as models_teacher
from course import models as models_course
from qualification import models as models_qualification


def createUser(data):
    try:
        estudiantes_creados = 0
        estudiantes_error = 0
        for fila in data.iter_rows(min_row=2, values_only=True):
            name = fila[0].lower()
            sex  = fila[1]
            age  = fila[2]
            address = fila[3]
            email = fila[4]

            if name and isinstance(name, str):
                if sex and isinstance(sex, str) and age and isinstance(age, int) and address and isinstance(address, str) and email and isinstance(email, str):
                    if not models_student.Student.objects.filter(name=name).exists():
                        models_student.Student.objects.create(
                            name=name,
                            sex=sex,
                            age=age,
                            address=address,
                            email=email
                        )
                        estudiantes_creados += 1
                    else:
                        estudiantes_error += 1
                else:
                    estudiantes_error += 1
            else:
                estudiantes_error += 1
                    
        return estudiantes_creados, estudiantes_error
    except Exception as e:
        estudiantes_error += 1
        return estudiantes_creados, estudiantes_error


def createTeacher(data):
    try:
        teacher_creados = 0
        teacher_error = 0
        for fila in data.iter_rows(min_row=2, values_only=True):
            name = fila[0].lower()
            sex = fila[1]
            age = fila[2]
            address = fila[3]
            email = fila[4]

            if name and isinstance(name, str):
                if sex and isinstance(sex, str) and age and isinstance(age, int) and address and isinstance(address, str) and email and isinstance(email, str):
                    if not models_teacher.Teacher.objects.filter(name=name).exists():
                        models_teacher.Teacher.objects.create(
                            name=name,
                            sex=sex,
                            age=age,
                            address=address,
                            email=email
                        )
                        teacher_creados += 1
                    else:
                        teacher_error += 1
                else:
                    teacher_error += 1
            else:
                teacher_error += 1
                    
        return teacher_creados, teacher_error
    except Exception as e:
        teacher_error += 1
        return teacher_creados, teacher_error


def createCourse(data):
    try:
        course_creados = 0
        course_error = 0
        for fila in data.iter_rows(min_row=2, values_only=True):
            course_scraped_name = fila[0].lower()
            teacher_name = fila[1].lower()
            student_name = fila[2].lower()

            # Obtener o crear el curso
            if not models_course_scraped.CursoScraped.objects.filter(name=course_scraped_name).exists():
                course_scraped = models_course_scraped.CursoScraped.objects.create(name=course_scraped_name)

            course_scraped = models_course_scraped.CursoScraped.objects.filter(name=course_scraped_name).first()

            if not models_teacher.Teacher.objects.filter(name=teacher_name).exists():
                models_teacher.Teacher.objects.create(name=teacher_name)

            teacher = models_teacher.Teacher.objects.filter(name=teacher_name).first()

            if not models_student.Student.objects.filter(name=student_name).exists():
                models_student.Student.objects.create(name=student_name)

            student = models_student.Student.objects.filter(name=student_name).first()

            if not models_course.Course.objects.filter(course_scraped=course_scraped).exists():
                course = models_course.Course.objects.create(
                    course_scraped=course_scraped,
                    teacher=teacher,
                )
                course.students.add(student)
            else:
                course = models_course.Course.objects.filter(course_scraped=course_scraped).first()
                course.students.add(student)
            
            course_creados += 1
                    
        return course_creados, course_error
    except Exception as e:
        course_error += 1
        return course_creados, course_error



def createQualification(data):
    try:
        quialification_creados = 0
        quialification_error = 0
        for fila in data.iter_rows(min_row=2, values_only=True):
            course_name = fila[0].lower()
            student = fila[1].lower()
            quialification = fila[2]

            if course_name and isinstance(course_name, str):
                if student and isinstance(student, str) and quialification and isinstance(quialification, int) :
                    if models_course.Course.objects.filter(course_scraped__name=course_name, students__name=student).exists():

                            get_course = models_course.Course.objects.filter(course_scraped__name=course_name, students__name=student).first()
                            get_student = models_student.Student.objects.filter(name=student).first()

                            if not models_qualification.Qualification.objects.filter(course=get_course, student=get_student).exists():
                                models_qualification.Qualification.objects.create(
                                    course=get_course,
                                    student=get_student,
                                    qualification=quialification
                                )

                                quialification_creados += 1

                    else:
                        quialification_error += 1
                else:
                    quialification_error += 1
            else:
                quialification_error += 1
                    
        return quialification_creados, quialification_error
    except Exception as e:
        teacher_error += 1
        return quialification_creados, quialification_error

    