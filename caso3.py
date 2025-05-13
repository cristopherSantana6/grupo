#Elabore un programa que procese las calificaciones de varios estudiantes de la carrera de Ingeniería en Sistemas de la Información en la UAM. Por cada estudiante, se ingresarán las calificaciones de tres asignaturas, y cada asignatura incluirá tres tareas y un examen. El programa debe calcular el promedio por asignatura y el promedio general del estudiante. Utilice estructuras cíclicas anidadas para manejar estudiantes, asignaturas y evaluaciones.

num_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))
num_asignaturas = int(input("Ingrese la cantidad de asignaturas: "))
num_examenes = int(input("Ingrese la cantidad de examenes: "))

for estudiante in range (num_estudiantes):
    total_estudiante = 0
    print(f"\nEstudiante {estudiante}:")
for asignatura in range (num_asignaturas):
    suma_notas = 0
    print(f"Asignaturas {asignatura}:")
for examen in range(num_examenes):
    nota = float(input(f"Nota del Examen {examen}"))
    
    suma_notas += nota
    promedio_asignatura = suma_notas/ num_examenes
    print(f"Promedio de Asignatura {asignatura}: {promedio_asignatura:.2f}")
    
    total_estudiante += promedio_asignatura
    promedio_estudiante = total_estudiante/num_asignaturas
    print(f"Promedio final del Estudiante {estudiante}: {promedio_estudiante:.2f}")