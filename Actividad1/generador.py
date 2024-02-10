import random  # Importamos el módulo random para generar números aleatorios

def generar_numeros_aleatorios(cantidad):
    """Genera una lista de números aleatorios."""
    numeros_aleatorios = []
    for _ in range(cantidad):
        numeros_aleatorios.append(random.randint(1, 100))  # Genera un número aleatorio y lo agrega a la lista
    return numeros_aleatorios
