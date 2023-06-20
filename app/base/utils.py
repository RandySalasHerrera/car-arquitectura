from student import models as models_student
from teacher import models as models_teacher


def createUser(data):
    try:
        estudiantes_creados = 0
        estudiantes_error = 0
        for fila in data.iter_rows(min_row=2, values_only=True):
            name = fila[0]
            sex = fila[1]
            age = fila[2]
            address = fila[3]
            email = fila[4]

            if name and isinstance(name, str):
                if sex and isinstance(sex, str) and age and isinstance(age, int) and address and isinstance(address, str) and email and isinstance(email, str):
                    if not models_student.Student.objects.filter(name=name, email=email).exists():
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
            name = fila[0]
            sex = fila[1]
            age = fila[2]
            address = fila[3]
            email = fila[4]

            if name and isinstance(name, str):
                if sex and isinstance(sex, str) and age and isinstance(age, int) and address and isinstance(address, str) and email and isinstance(email, str):
                    if not models_teacher.Teacher.objects.filter(name=name, email=email).exists():
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

    