"""Caso 9: Evaluación del acceso a internet en hogares de estudiantes
Implemente un programa que simule una encuesta realizada a estudiantes de la UAM para
conocer su acceso a internet en casa. Se trabajará con tres carreras, cada una con tres grupos,
y se entrevistará a cinco estudiantes por grupo. Se debe registrar si el estudiante tiene acceso
estable, intermitente o no tiene internet. Al final, mostrar un conteo de cada tipo de acceso por
carrera y el total general.
"""

carreras = ["Sistemas", "Marketing", "Derecho"]
tipos_acceso = ["estable", "intermitente", "no tiene"]

conteo_por_carrera = []

total_general = {"estable": 0, "intermitente": 0, "no tiene": 0}

for carrera in carreras:
    print(f"\nCarrera: {carrera}")
    conteo = {"estable": 0, "intermitente": 0, "no tiene": 0}

    for grupo in range(1, 4):
        print(f"  Grupo {grupo}")

        for estudiante in range(1, 6):
            while True:
                acceso = input(f"Estudiante {estudiante} ¿Acceso a internet? (estable/intermitente/no tiene): ").lower()
                if acceso in tipos_acceso:
                    conteo[acceso] += 1
                    total_general[acceso] += 1
                    break
                else:
                    print("    Opción inválida. Intente de nuevo.")
    
    conteo_por_carrera.append((carrera, conteo))

print("\n--- Resultados por carrera ---")
for carrera, datos in conteo_por_carrera:
    print(f"\nCarrera: {carrera}")
    for tipo in tipos_acceso:
        print(f"  {tipo.capitalize()}: {datos[tipo]} estudiantes")

print("\n--- Totales generales ---")
for tipo in tipos_acceso:
    print(f"{tipo.capitalize()}: {total_general[tipo]} estudiantes")
