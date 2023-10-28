def es_seguro(tablero, fila, columna, n):
    # Verifica si es seguro colocar una reina en la posición (fila, columna)
    # Verifica la misma columna
    for i in range(fila):
        if tablero[i][columna] == 1:
            return False
    # Verifica la diagonal superior izquierda
    for i, j in zip(range(fila, -1, -1), range(columna, -1, -1)):
        if tablero[i][j] == 1:
            return False
    # Verifica la diagonal superior derecha
    for i, j in zip(range(fila, -1, -1), range(columna, n)):
        if tablero[i][j] == 1:
            return False
    return True

def resolver_n_reinas(n):
    tablero = [[0] * n for _ in range(n)]

    def backtrack(fila):
        if fila == n:
            # Se encontró una solución
            for fila_actual in tablero:
                print(fila_actual)
            print()
        else:
            for columna in range(n):
                if es_seguro(tablero, fila, columna, n):
                    tablero[fila][columna] = 1
                    backtrack(fila + 1)
                    tablero[fila][columna] = 0

    backtrack(0)

n = 4  # Tamaño del tablero NxN
resolver_n_reinas(n)
