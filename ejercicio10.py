"""Caso 10: Control de préstamos en la biblioteca de la UAM
Desarrolle un programa que permita registrar los préstamos de libros en la biblioteca de la UAM.
Se trabajará con cuatro categorías de libros (ingeniería, salud, derecho y literatura), cada una
con tres subcategorías. Por cada subcategoría se registrarán los préstamos de cinco días. El
sistema debe mostrar el total de préstamos por subcategoría, categoría y el total general
semanal."""

categorias = {
    "Ingeniería": ["Civil", "Sistemas", "Industrial"],
    "Salud": ["Enfermería", "Medicina", "Nutrición"],
    "Derecho": ["Penal", "Civil", "Laboral"],
    "Literatura": ["Poesía", "Narrativa", "Ensayo"]}

total_general = 0 

for categoria, subcategorias in categorias.items():
    print(f"\nCategoría: {categoria}")
    total_categoria = 0

    for sub in subcategorias:
        print(f"  Subcategoría: {sub}")
        total_sub = 0

        for dia in range(1, 6):
            cantidad = int(input(f" Día {dia} - Libros prestados: "))
            total_sub += cantidad

        print(f"Total en subcategoría {sub}: {total_sub} libros")
        total_categoria += total_sub

    print(f"Total en categoría {categoria}: {total_categoria} libros")
    total_general += total_categoria

print(f"\nTotal general de préstamos en la semana: {total_general} libros")
