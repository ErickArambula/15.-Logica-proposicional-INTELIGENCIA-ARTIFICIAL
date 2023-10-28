# Importar itertools para generar todas las combinaciones de P y Q
import itertools

# Definir las variables P y Q
variables = ['P', 'Q']

# Generar todas las combinaciones posibles de valores para P y Q (V y F)
combinations = list(itertools.product([True, False], repeat=2))

# Imprimir el encabezado de la tabla de verdad
print("| P | Q | (P AND Q) OR (NOT P) |")

# Evaluar la expresión lógica para cada combinación de valores
for combo in combinations:
    P, Q = combo
    result = (P and Q) or (not P)
    
    # Imprimir la fila de la tabla de verdad
    print(f"| {str(P)[0]} | {str(Q)[0]} | {str(result)[0]} |")
