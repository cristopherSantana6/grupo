"""
Caso 4: Registro de participación estudiantil por carrera en la UAM
Desarrolle un programa que registre la participación de estudiantes de la UAM en actividades
extracurriculares por carrera. Considere tres carreras (por ejemplo: Sistemas, Marketing y
Derecho), cada una con tres años académicos, y cada año con dos secciones. Por cada
sección, se debe registrar cuántos estudiantes participaron. El programa debe mostrar el total
por carrera y el total general de participantes. Utilice bucles anidados.
"""

carreras = ["Sistemas", "Marketing", "Derecho"]
años = ["1er Año", "2do Año", "3er Año"]
secciones = ["A", "B"]
total_general = 0

for carrera in carreras:
    print(f"\nRegistrando participación para la carrera de {carrera}")
    total_carrera = 0

    for año in años:
        for seccion in secciones:
            mensaje = f"Ingrese la cantidad de estudiantes en {carrera} - {año} - Sección {seccion}: "
            cantidad = int(input(mensaje))
            total_carrera += cantidad
            
    print(f"Total de participantes en {carrera}: {total_carrera}")
    total_general += total_carrera

print(f"\nTotal general de participantes: {total_general}")
