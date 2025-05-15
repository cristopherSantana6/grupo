"""
Caso 5: Encuesta sobre transporte estudiantil en la UAM
Implemente un programa que simule una encuesta realizada en la UAM para conocer los medios
de transporte utilizados por los estudiantes. Considere tres facultades, cada una con dos
carreras, y en cada carrera se entrevistarán a cinco estudiantes. Por cada estudiante se debe
registrar si utiliza bus, motocicleta, taxi, bicicleta o camina. Al final, se mostrarán los totales por
medio de transporte, desglosados por facultad y el total general. Utilice estructuras cíclicas
anidadas.
"""
# Facultades y carreras
facultades = ["Ingeniería", "Ciencias Económicas", "Derecho"]
carreras_por_facultad = [
    ["Sistemas", "Industrial"],
    ["Marketing", "Contaduría"],
    ["Derecho Penal", "Derecho Civil"]]

transportes = ["bus", "motocicleta", "taxi", "bicicleta", "camina"]

totales_facultad = []
total_general = {t: 0 for t in transportes}

for i in range(len(facultades)):
    facultad = facultades[i]
    carreras = carreras_por_facultad[i]
    print(f"\nFacultad: {facultad}")

    contador_facultad = {t: 0 for t in transportes}

    for carrera in carreras:
        print(f"\nCarrera: {carrera}")

        for estudiante in range(1, 6):
            while True:
                transporte = input(f"Estudiante {estudiante}, ¿qué medio de transporte usas? (bus/motocicleta/taxi/bicicleta/camina): ").lower()
                if transporte in transportes:
                    contador_facultad[transporte] += 1
                    total_general[transporte] += 1
                    break
                else:
                    print("Opción inválida. Intente de nuevo.")

    totales_facultad.append((facultad, contador_facultad))

print("\n--- Resultados por Facultad ---")
for facultad, conteo in totales_facultad:
    print(f"\nFacultad: {facultad}")
    for t in transportes:
        print(f"{t.capitalize()}: {conteo[t]}")

print("\n--- Total General ---")
for t in transportes:
    print(f"{t.capitalize()}: {total_general[t]}")
