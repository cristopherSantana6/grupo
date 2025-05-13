#Cree un programa que simule el control de gastos semanales de un grupo de estudiantes de
#primer año de la UAM. El sistema debe procesar datos de 4 semanas, y por cada semana,
#ingresar el gasto realizado cada día (7 días por semana). El programa debe calcular el total
#gastado por semana y el total acumulado del mes. Utilice bucles anidados para recorrer
#semanas y días.

total_mes = 0  # Inicializa el total acumulado del mes
gastos_semanales = 4  # Número de semanas
gastos_dia = 7  # Número de días por semana
for mes in range (1, 5):  # Itera sobre las semanas (1 a 4)
    total_semana = 0  # Inicializa el total de la semana
    print(f"\nSemana {mes}:")
    for dia in range(1, 8):  # Itera sobre los días (1 a 7)
        gasto = float(input(f"Ingrese el gasto del día {dia}: "))  # Solicita el gasto del día
        total_semana += gasto  # Suma el gasto al total de la semana
    print(f"Total gastado en la semana {mes}: {total_semana:.2f}")  # Muestra el total de la semana
    total_mes += total_semana  # Suma el total de la semana al total acumulado del mes
print(f"\nTotal acumulado del mes: {total_mes:.2f}")  # Muestra el total acumulado del mes
