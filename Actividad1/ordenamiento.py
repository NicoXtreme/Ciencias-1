import time
def ordenamiento_burbuja(lista):
    n = len(lista)
    comparaciones = 0 
    intercambios = 0
    pasos = 0
    for i in range(n):
        for j in range(0, n-i-1):
            comparaciones +=1
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                intercambios+=1
                pasos+=3
            pasos +=3
        pasos +=4
    pasos+=2

    print(f"Pasos realizados: {pasos}")        
    print(f"Comparaciones realizadas: {comparaciones}")
    print(f"Intercambios realizados: {intercambios}")



def ord_seleccion(lista):
    comparaciones = 0 
    intercambios = 0
    pasos= 0
    for i in range(len(lista) - 1):        # <-- bucle padre
        menor = i # primer elemento por default será el mínimo
        
        for j in range(i + 1, len(lista)): # <-- bucle hijo
            comparaciones +=1
            pasos+=1
            if lista[j] < lista[menor]:
                menor = j
                intercambios+=1
                

        if menor != i:
            lista[menor], lista[i] = lista[i], lista[menor]
            pasos+=1
        pasos+=1
    pasos+=2    

    print(f"Pasos realizados: {pasos}")
    print(f"Comparaciones realizadas: {comparaciones}")
    print(f"Intercambios realizados: {intercambios}")