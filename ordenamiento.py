import time

def ord_burbuja(lista):
    inicio = time.perf_counter()
    n = len(lista)
    ciclos = 0 
    pasos = 0
    for i in range(n):
        for j in range(0, n-i-1):
            ciclos += 1
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                pasos += 3
            pasos += 3
        pasos += 4
    pasos += 2
    fin = time.perf_counter()
    tiempo_total = fin - inicio

    print(f"Pasos realizados: {pasos}")        
    print(f"Ciclos realizados: {ciclos}")
    print(f"Tiempo de ejecución: {tiempo_total} segundos")

def ord_seleccion(lista):
    inicio = time.perf_counter()
    ciclos = 0 
    pasos = 0
    for i in range(len(lista) - 1):        # <-- bucle padre
        menor = i # primer elemento por default será el mínimo
        
        for j in range(i + 1, len(lista)): # <-- bucle hijo
            ciclos += 1
            pasos += 1
            if lista[j] < lista[menor]:
                menor = j

        if menor != i:
            lista[menor], lista[i] = lista[i], lista[menor]
            pasos += 1
        pasos += 1
    pasos += 2
    fin = time.perf_counter()
    tiempo_total = fin - inicio

    print(f"Pasos realizados: {pasos}")
    print(f"Ciclos realizados: {ciclos}")
    print(f"Tiempo de ejecución: {tiempo_total} segundos")

def ord_insercion(lista):
    inicio = time.perf_counter()
    n = len(lista)
    ciclos = 0 
    pasos = 0
    for i in range(1, len(lista)):
        valor_actual = lista[i]
        posicion = i

        while posicion > 0 and lista[posicion - 1] > valor_actual:
            lista[posicion] = lista[posicion - 1]
            posicion -= 1
            pasos += 1

        lista[posicion] = valor_actual
        ciclos += 1  

    fin = time.perf_counter()
    tiempo_total = fin - inicio

    print(f"Pasos realizados: {pasos}")        
    print(f"Ciclos realizados: {ciclos}")
    print(f"Tiempo de ejecución: {tiempo_total:.6f} segundos")

def ord_heapsort(lista):
    inicio = time.perf_counter()
    pasos = 0
    ciclos = 0

    def heapify(lista, size, index):
        nonlocal ciclos, pasos
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        # Realizar comparaciones
        pasos += 1

        if left < size and lista[left] > lista[largest]:
            largest = left

        if right < size and lista[right] > lista[largest]:
            largest = right

        if largest != index:
            # Realizar intercambio
            lista[index], lista[largest] = lista[largest], lista[index]
            # Recursivamente llama a heapify en el subárbol afectado
            heapify(lista, size, largest)

    size = len(lista)

    # Construir un max-heap
    for i in range(size // 2 - 1, -1, -1):
        ciclos += 1
        heapify(lista, size, i)

    # Extraer elementos uno por uno
    for i in range(size - 1, 0, -1):
        # Realizar intercambio
        lista[0], lista[i] = lista[i], lista[0]
        # Reorganizar el heap
        heapify(lista, i, 0)
        ciclos += 1

    fin = time.perf_counter()
    tiempo_total = fin - inicio

    print(f"Pasos realizados: {pasos}")
    print(f"Ciclos realizados: {ciclos}")
    print(f"Tiempo de ejecución: {tiempo_total:.6f} segundos")


def ord_mergesort(lista):
    inicio = time.perf_counter()
    pasos = 0
    ciclos = 0

    

    fin = time.perf_counter()
    tiempo_total = fin - inicio

    print(f"Pasos realizados: {pasos}")
    print(f"Ciclos realizados: {ciclos}")
    print(f"Tiempo de ejecución: {tiempo_total:.6f} segundos")

    def merge(lista):    
        if len(lista) > 1:
            medio = len(lista) // 2
            izq = lista[:medio]
            der = lista[medio:]

            merge(izq)
            merge(der)

            i, j, k = 0, 0, 0

            while i < len(izq) and j < len(der):
                if izq[i] <= der[j]:
                    lista[k] = izq[i]
                    i += 1
                else:
                    lista[k] = der[j]
                    j += 1
                k += 1

            while i < len(izq):
                lista[k] = izq[i]
                i += 1
                k += 1

            while j < len(der):
                lista[k] = der[j]
                j += 1
                k += 1
    merge(lista)

    fin = time.perf_counter()
    tiempo_total = fin - inicio

    print(f"Pasos realizados: {pasos}")
    print(f"Ciclos realizados: {ciclos}")
    print(f"Tiempo de ejecución: {tiempo_total:.6f} segundos")

