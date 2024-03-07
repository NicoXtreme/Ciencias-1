def suma_maxima(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])

    if filas == 0 or columnas == 0:
        return []

    maximos = [0] * filas
    for i, fila in enumerate(matriz):
        n = len(fila)
        if n == 0:
            maximos[i] = 0
        elif n == 1:
            maximos[i] = fila[0]
        else:
            incluido = fila[0]
            excluido = 0

            for j in range(1, n):
                nueva_incluido = excluido + fila[j]

                excluido = max(incluido, excluido)
                incluido = nueva_incluido

            maximos[i] = max(incluido, excluido)

    return maximos

matriz = [[1, 8, 2, 1, 9],
          [1, 7, 3, 5, 2],
          [1, 2, 10, 3, 10],
          [8, 4, 7, 9, 1],
          [7, 1, 3, 1, 6]]

resultado_obtenido = suma_maxima(matriz)
print("Sumas maximas de cada fila:", resultado_obtenido)

# Aplicar el proceso nuevamente a la nueva lista obtenida
nueva_lista = resultado_obtenido
nuevo_resultado = suma_maxima([nueva_lista])

print("Maximos dulces posibles teniendo en cuenta la restriccion:", nuevo_resultado)
