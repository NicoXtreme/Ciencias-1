import random

def generar_numeros_aleatorios(cantidad, rango_maximo):
    """Genera una lista de números aleatorios dentro del rango especificado."""
    numeros_aleatorios = []
    for _ in range(cantidad):
        numero_aleatorio = random.randint(1, rango_maximo)  # Genera un número aleatorio entre 1 y el rango máximo
        numeros_aleatorios.append(numero_aleatorio)  # Agrega el número a la lista
    return numeros_aleatorios
