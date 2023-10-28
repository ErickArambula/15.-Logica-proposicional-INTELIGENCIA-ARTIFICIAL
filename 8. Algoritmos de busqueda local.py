import random

# Función de ejemplo: f(x) = -x^2
def funcion_objetivo(x):
    return -x**2

def hill_climbing(funcion_objetivo, valor_inicial, iteraciones):
    mejor_solucion = valor_inicial

    for _ in range(iteraciones):
        vecino = mejor_solucion + random.uniform(-0.1, 0.1)  # Generar un vecino cercano

        # Si el vecino es mejor que la solución actual, actualiza la solución
        if funcion_objetivo(vecino) > funcion_objetivo(mejor_solucion):
            mejor_solucion = vecino

    return mejor_solucion

# Parámetros iniciales
valor_inicial = 2.0  # Valor inicial aleatorio
iteraciones = 100  # Número de iteraciones

# Ejecutar Hill Climbing
solucion_optima = hill_climbing(funcion_objetivo, valor_inicial, iteraciones)

# Imprimir la solución encontrada
print("Solución óptima encontrada:", solucion_optima)
print("Valor óptimo:", funcion_objetivo(solucion_optima))
