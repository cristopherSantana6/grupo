#Cree un programa que simule el control de gastos semanales de un grupo de estudiantes de
#primer año de la UAM. El sistema debe procesar datos de 4 semanas, y por cada semana,
#ingresar el gasto realizado cada día (7 días por semana). El programa debe calcular el total
#gastado por semana y el total acumulado del mes. Utilice bucles anidados para recorrer
#semanas y días.

total_mes = 0  # Inicializa el total acumulado del mes
gastos_semanales = 4  # Número de semanas
gastos_dia = 7  # Número de días por semana
for semana in range(gastos_semanales):
    print(f"\nSemana {semana + 1}:")
    total_semana = 0  # Inicializa el total de la semana
    for dia in range(gastos_dia):
        gasto_dia = float(input(f"Ingrese el gasto del día {dia + 1}: "))
        total_semana += gasto_dia 
        total_mes += total_semana  # Acumula el total del mes
    print(f"Total gastado en la semana {semana + 1}: C${total_semana:.2f}")
    print(f"Total acumulado del mes {total_mes:.2f}")
