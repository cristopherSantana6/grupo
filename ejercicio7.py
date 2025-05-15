"""Caso 7: Control de ventas en kioscos estudiantiles de la UAM
Implemente un programa que simule el control de ventas de alimentos en tres kioscos dentro
del campus UAM. Cada kiosco ofrece cinco productos diferentes y se registrarán las ventas
durante cuatro días. El programa debe calcular y mostrar el total vendido por producto en cada
kiosco, así como el total general por día."""

kioscos = ["Kiosco 1", "Kiosco 2", "Kiosco 3"]
productos = ["Galletas", "Jugos", "Empanadas", "Sándwiches", "Nacatamales"]

ventas_kioscos = [[[0 for _ in range(5)] for _ in range(4)] for _ in range(3)]

for dia in range(4):
    print(f"\n--- Día {dia + 1} ---")
    total_dia = 0

    for i in range(3):  
        print(f"\n{kioscos[i]}")
        for j in range(5):  
            mensaje = f"¿Cuántos {productos[j]} se vendieron en el Día {dia + 1}? "
            cantidad = int(input(mensaje))
            ventas_kioscos[i][dia][j] = cantidad
            total_dia += cantidad

    print(f"Total general vendido en el Día {dia + 1}: {total_dia} productos")

print("\n--- Totales por producto en cada kiosco ---")
for i in range(3):  
    print(f"\n{kioscos[i]}")
    for j in range(5):  
        total_producto = 0
        for dia in range(4):
            total_producto += ventas_kioscos[i][dia][j]
        print(f"{productos[j]}: {total_producto} vendidos en total")
