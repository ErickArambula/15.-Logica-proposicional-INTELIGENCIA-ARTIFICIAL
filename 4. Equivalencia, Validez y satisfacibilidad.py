import sympy as sp

# Definir las variables P y Q
P, Q = sp.symbols('P Q')

# Expresiones lógicas
expresion_1 = P & Q
expresion_2 = Q & P

# Verificar la equivalencia
equivalencia = sp.Equivalent(expresion_1, expresion_2)
print("¿Las expresiones son equivalentes?", equivalencia)

# Verificar la validez
validez = sp.validity(expresion_1)
print("¿La expresión 1 es válida?", validez)

# Verificar la satisfacibilidad
satisfacibilidad = sp.satisfiable(expresion_1)
print("¿La expresión 1 es satisfacible?", satisfacibilidad)
