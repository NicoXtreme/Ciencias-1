import time

def ordenamiento_burbuja(lista):
    inicio = time.time()  # Registra el tiempo de inicio
    n = len(lista)
    comparaciones = 0 
    intercambios = 0
    pasos = 0
    for i in range(n):
        for j in range(0, n-i-1):
            comparaciones += 1
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                intercambios += 1
                pasos += 3
            pasos += 3
        pasos += 4
    pasos += 2
    fin = time.time()  
    tiempo_total = fin - inicio  # Calcula el tiempo total de ejecución

    print(f"Pasos realizados: {pasos}")        
    print(f"Comparaciones realizadas: {comparaciones}")
    print(f"Intercambios realizados: {intercambios}")
    print(f"Tiempo de ejecución: {tiempo_total} segundos")

def ord_seleccion(lista):
    inicio = time.time()  # Registra el tiempo de inicio
    comparaciones = 0 
    intercambios = 0
    pasos = 0
    for i in range(len(lista) - 1):        # <-- bucle padre
        menor = i # primer elemento por default será el mínimo
        
        for j in range(i + 1, len(lista)): # <-- bucle hijo
            comparaciones += 1
            pasos += 1
            if lista[j] < lista[menor]:
                menor = j
                intercambios += 1

        if menor != i:
            lista[menor], lista[i] = lista[i], lista[menor]
            pasos += 1
        pasos += 1
    pasos += 2
    fin = time.time()  
    tiempo_total = fin - inicio  # Calcula el tiempo total de ejecución

    print(f"Pasos realizados: {pasos}")
    print(f"Comparaciones realizadas: {comparaciones}")
    print(f"Intercambios realizados: {intercambios}")
    print(f"Tiempo de ejecución: {tiempo_total} segundos")

def ord_heapsort(lista):
    inicio = time.perf_counter()
    comparaciones = 0
    intercambios = 0
    pasos = 0

    def heapify(lista, size, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < size and lista[left] > lista[largest]:
            largest = left

        if right < size and lista[right] > lista[largest]:
            largest = right

        if largest != index:
            lista[index], lista[largest] = lista[largest], lista[index]
            heapify(lista, size, largest)

    size = len(lista)

    # Construir un max-heap
    for i in range(size // 2 - 1, -1, -1):
        heapify(lista, size, i)

    # Extraer elementos uno por uno
    for i in range(size - 1, 0, -1):
        lista[0], lista[i] = lista[i], lista[0]
        heapify(lista, i, 0)

    fin = time.perf_counter()
    tiempo_total = fin - inicio

    print(f"Pasos realizados: {pasos}")
    print(f"Comparaciones realizadas: {comparaciones}")
    print(f"Intercambios realizados: {intercambios}")
    print(f"Tiempo de ejecución: {tiempo_total:.6f} segundos")



