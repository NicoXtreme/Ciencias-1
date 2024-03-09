def suma_maxima(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])

    if filas == 0 or columnas == 0:
        return [], 0  

    maximos = [0] * filas
    pasos = 0  
    for fila in matriz:
        n = len(fila)
        if n == 0:
            pasos += 1  
            continue  
        elif n == 1:
            maximos[pasos] = fila[0]
            pasos += 1
            continue  
        else:
            incluido = fila[0]
            excluido = 0

            for j in range(1, n):
                nueva_incluido = excluido + fila[j]
                excluido = max(incluido, excluido)
                incluido = nueva_incluido

            maximos[pasos] = max(incluido, excluido)
            pasos += 1  

    return maximos, pasos  

matriz = [[1, 8, 2, 1, 9],
          [1, 7, 3, 5, 2],
          [1, 2, 10, 3, 10],
          [8, 4, 7, 9, 1],
          [7, 1, 3, 1, 6]]

resultado_obtenido, pasos = suma_maxima(matriz)
print("Sumas máximas de cada fila:", resultado_obtenido)
print("Pasos realizados:", pasos)

nueva_lista = resultado_obtenido
nuevo_resultado, pasos_nuevo = suma_maxima([nueva_lista])

print("Máximos dulces posibles teniendo en cuenta la restricción: (Respuesta)", nuevo_resultado)
print("Pasos realizados en el nuevo cálculo:", pasos_nuevo)

