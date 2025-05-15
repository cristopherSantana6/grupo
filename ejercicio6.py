"""Caso 6: Registro de ventas de nacatamales en eventos de domingo en la UAM
Cree un programa que simule la venta de nacatamales durante cuatro domingos consecutivos
en actividades realizadas en la UAM (como torneos, convivencias o ferias). Por cada domingo,
se deberá registrar la cantidad de clientes y cuántos nacatamales compró cada uno. El
programa debe calcular el total vendido por domingo y el acumulado mensual. Utilice bucles
anidados para domingos y clientes"""

total_mensual = 0

for domingo in range(1, 5):
    print(f"\nDomingo {domingo}")
    total_dia = 0

    clientes = int(input("¿Cuántos clientes compraron nacatamales este domingo? "))

    for cliente in range(1, clientes + 1):
        cantidad = int(input(f"Cliente {cliente}: ¿Cuántos nacatamales compró? "))
        total_dia += cantidad

    print(f"Total vendido en el Domingo {domingo}: {total_dia} nacatamales")
    total_mensual += total_dia

print(f"\nTotal vendido en el mes: {total_mensual} nacatamales")
