from generador import generar_numeros_aleatorios
from ordenamiento import *

try:
    opcion = int(input("Seleccione la opción para generar números aleatorios:\n1. Generar 100 números aleatorios\n2. Generar 1000 números aleatorios\n3. Generar 10000 números aleatorios\nIngrese el número de la opción: "))

    if opcion == 1:
        cantidad_numeros = 100
        rango = (1, 100)  # Rango para 100 números
    elif opcion == 2:
        cantidad_numeros = 1000
        rango = (1, 1000)  # Rango para 1000 números
    elif opcion == 3:
        cantidad_numeros = 10000
        rango = (1, 10000)  # Rango para 10000 números
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
    metodo_ordenamiento = input("Seleccione el método de ordenamiento (burbuja, seleccion, insercion o heap): ").lower()
    if metodo_ordenamiento == "burbuja":
        ord_burbuja(numeros_generados)
    elif metodo_ordenamiento == "seleccion":
        ord_seleccion(numeros_generados)
    elif metodo_ordenamiento == "insercion":
        ord_insercion(numeros_generados)    
    elif metodo_ordenamiento == "heap":
        ord_heapsort(numeros_generados)        
    else:
        print("Método de ordenamiento no válido.")

    # Guardar números ordenados en un archivo
    with open("numeros_ordenados.txt", "w") as archivo_ordenado:
        for numero in numeros_generados:
            archivo_ordenado.write(str(numero) + "\n")
    print("Números aleatorios ordenados guardados en 'numeros_ordenados.txt'")

except ValueError:
    print("Por favor, ingrese un número válido.")

