"""Caso 8: Registro de consumo eléctrico por edificio en la UAM
Desarrolle un programa que permita registrar el consumo eléctrico de cinco edificios del campus
UAM (como aulas, biblioteca, administración, laboratorios y cafetería) durante tres turnos del
día (mañana, tarde y noche), por una semana. El programa debe mostrar el consumo por edificio
y el total general semanal."""

edificios = ["Aulas", "Biblioteca", "Administración", "Laboratorios", "Cafetería"]
turnos = ["Mañana", "Tarde", "Noche"]

consumo = [[[0 for _ in range(3)] for _ in range(7)] for _ in range(5)]

for e in range(5):  
    print(f"\nRegistro para el edificio: {edificios[e]}")
    for d in range(7): 
        print(f"Día {d + 1}:")
        for t in range(3):  
            mensaje = f"Ingrese consumo en kWh del turno {turnos[t]}: "
            valor = float(input(mensaje))
            consumo[e][d][t] = valor

total_general = 0
print("\n--- Consumo total por edificio en la semana ---")
for e in range(5):
    total_edificio = 0
    for d in range(7):
        for t in range(3):
            total_edificio += consumo[e][d][t]
    print(f"{edificios[e]}: {total_edificio:.2f} kWh")
    total_general += total_edificio

print(f"\nTotal general de consumo eléctrico en la semana: {total_general:.2f} kWh")
