import time

def ordenamiento_burbuja(lista):
    """Implementación del algoritmo de ordenamiento de burbuja."""
    inicio = time.time()  # Registra el tiempo de inicio
    n = len(lista)
    ciclos = 0  # Contador de ciclos
    intercambios = 0  # Contador de intercambios
    pasos = 0  # Contador total de pasos
    for i in range(n):  
        for j in range(0, n-i-1):  
            ciclos += 1  
            if lista[j] > lista[j+1]:  
                lista[j], lista[j+1] = lista[j+1], lista[j]  
                intercambios += 1  
            pasos += 3  # Comparación e intercambio
        pasos += 4  # Operaciones al final del bucle interno
    pasos += 2  # Operaciones fuera de los bucles

    fin = time.time()  
    tiempo_total = fin - inicio  

    # Impresión de resultados
    print(f"Pasos realizados: {pasos}")        
    print(f"Ciclos realizados: {ciclos}")  
    print(f"Intercambios realizados: {intercambios}")
    print(f"Tiempo de ejecución: {tiempo_total} segundos")

import time

def ord_seleccion(lista):
    """Implementación del algoritmo de ordenamiento por selección."""
    inicio = time.time()  
    ciclos = 0  
    intercambios = 0 
    pasos = 0  # Inicialización del contador de pasos
    for i in range(len(lista) - 1):      
        menor = i
        pasos += 1  # Incrementa el contador de pasos al iniciar una nueva iteración del bucle externo
        for j in range(i + 1, len(lista)):
            ciclos += 1  
            pasos += 1  # Incrementa el contador de pasos por cada iteración del bucle interno
            if lista[j] < lista[menor]:
                menor = j
                intercambios += 1  # Incrementa el contador de intercambios
                pasos += 1  # Incrementa el contador de pasos por realizar un intercambio

        if menor != i:
            lista[menor], lista[i] = lista[i], lista[menor]  # Intercambia los elementos si es necesario
               
        pasos += 1  # Añade 1 paso adicional por finalizar la iteración del bucle externo

    fin = time.time()  
    tiempo_total = fin - inicio  

    # Impresion de resultados
    print(f"Pasos realizados: {pasos}")
    print(f"ciclos realizadas: {ciclos}")
    print(f"Intercambios realizados: {intercambios}")
    print(f"Tiempo de ejecución: {tiempo_total} segundos") 
