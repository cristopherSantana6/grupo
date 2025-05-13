"""
Caso 3: Cálculo de promedio académico en la UAM
Elabore un programa que procese las calificaciones de varios estudiantes de la carrera de
Ingeniería en Sistemas de la Información en la UAM. Por cada estudiante, se ingresarán las
calificaciones de tres asignaturas, y cada asignatura incluirá tres tareas y un examen. El
programa debe calcular el promedio por asignatura y el promedio general del estudiante. Utilice
estructuras cíclicas anidadas para manejar estudiantes, asignaturas y evaluaciones.
"""

num_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))

for estudiante in range(1, num_estudiantes + 1):
    print(f"\nEstudiante {estudiante}")
    promedio_total = 0

    for asignatura in range(1, 4):  
        print(f"\nAsignatura {asignatura}")
        suma_tareas = 0

        for tarea in range(1, 4):  
            nota_tarea = float(input(f"Ingrese la nota de la tarea {tarea}: "))
            suma_tareas += nota_tarea

        nota_examen = float(input("Ingrese la nota del examen: "))

        promedio_asignatura = (suma_tareas + nota_examen) / 4
        print(f"Promedio de la asignatura {asignatura}: {promedio_asignatura:.2f}")

        promedio_total += promedio_asignatura

    promedio_general = promedio_total / 3
    print(f"\nPromedio general del estudiante {estudiante}: {promedio_general:.2f}")