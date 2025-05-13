#Cree un programa que simule el control de gastos semanales de un grupo de estudiantes de primer año de la UAM. El sistema debe procesar datos de 4 semanas, y por cada semana,ingresar el gasto realizado cada día (7 días por semana). El programa debe calcular el total gastado por semana y el total acumulado del mes. Utilice bucles anidados para recorrer semanas y días.

num_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))
semanas = 4
dias = 7

for estudiante in range(num_estudiantes):
    total_mensual = 0
    print(f"\nEstudiante {estudiante}:")
    for semana in range(semanas):
        total_semanal = 0
        print(f" Semana {semana}:")
        for dia in range(dias):
            gasto = float(input(f"  Día {dia} - Gasto: $"))
            total_semanal += gasto
        print(f"  Total semanal: ${total_semanal:.2f}")
        total_mensual += total_semanal
    print(f" Total mensual del estudiante {estudiante}: ${total_mensual:.2f}")
