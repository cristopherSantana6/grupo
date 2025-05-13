"""
Caso 2: Registro semanal de gastos de estudiantes UAM
Cree un programa que simule el control de gastos semanales de un grupo de estudiantes de
primer año de la UAM. El sistema debe procesar datos de 4 semanas, y por cada semana,
ingresar el gasto realizado cada día (7 días por semana). El programa debe calcular el total
gastado por semana y el total acumulado del mes. Utilice bucles anidados para recorrer
semanas y días.
"""
total_mensual = 0

for semana in range(1, 5):  
    total_semanal = 0
    print(f"\nSemana {semana}:")
    for dia in range(1, 8):  
        gasto = float(input(f"Ingrese el gasto del día {dia}: "))
        total_semanal += gasto
    print(f"Total de gastos en la semana {semana}: {total_semanal}")
    total_mensual += total_semanal