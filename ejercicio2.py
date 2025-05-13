#Registro semanal de gastos de estudiantes UAM

gastos_semanales = 4
total_mes = 0
gastos_día = 7
for semana in range (1,):
    print(f"\nSemana {semana + 1}: ")
    total_semana = 0
    for día in range (gastos_día):
        gasto_día = float(input("Ingrese los datos del primer día: "))
        total_semana += gasto_día
        print(f"El monto total de los gastos enla semana {semana + 1}: C${total_semana:.2f}")
else:        
    total_mes += total_semana
    print(f"El monto total de los gastos del mes es {total_mes:.2f}")