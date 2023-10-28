import sympy as sp

# Definir símbolos
A, B, C = sp.symbols('A B C')

# Crear las cláusulas
clausula1 = A | B
clausula2 = ~A | C
clausula3 = B | C

# Aplicar la resolución
resolucion = sp.resolve([clausula1, clausula2, clausula3], [C])
resultado = resolucion[0]

# Imprimir el resultado
if resultado:
    print("C es verdadero cuando A es verdadero.")
else:
    print("No se puede inferir si C es verdadero cuando A es verdadero.")
