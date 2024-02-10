from generador import generar_numeros_aleatorios
from ordenamiento import ordenamiento_burbuja, ord_seleccion

# Menu
try:
    opcion = int(input("Seleccione la opción para generar números aleatorios:\n1. Generar 100 números aleatorios\n2. Generar 1000 números aleatorios\n3. Generar 10000 números aleatorios\nIngrese el número de la opción: "))

    if opcion == 1:
        cantidad_numeros = 100
    elif opcion == 2:
        cantidad_numeros = 1000
    elif opcion == 3:
        cantidad_numeros = 10000
    else:
        print("Por favor, seleccione una opción válida.")
        exit()

    numeros_generados = generar_numeros_aleatorios(cantidad_numeros)

    # Guardar números sin ordenar en un archivo
    with open("numeros_sin_ordenar.txt", "w") as archivo_sin_ordenar:
        for numero in numeros_generados:
            archivo_sin_ordenar.write(str(numero) + "\n")
        print("Números aleatorios generados sin ordenar guardados en 'numeros_sin_ordenar.txt'")

    # Ordenar los números
    metodo_ordenamiento = input("Seleccione el método de ordenamiento (burbuja o seleccion): ").lower()
    if metodo_ordenamiento == "burbuja":
        ordenamiento_burbuja(numeros_generados)
    elif metodo_ordenamiento == "seleccion":
        ord_seleccion(numeros_generados)
    else:
        print("Método de ordenamiento no válido. Se utilizará el método de burbuja por defecto.")

    # Guardar números ordenados en un archivo
    with open("numeros_ordenados.txt", "w") as archivo_ordenado:
        for numero in numeros_generados:
            archivo_ordenado.write(str(numero) + "\n")
        print("Números aleatorios ordenados guardados en 'numeros_ordenados.txt'")

except ValueError:
    print("Por favor, ingrese un número válido.")
