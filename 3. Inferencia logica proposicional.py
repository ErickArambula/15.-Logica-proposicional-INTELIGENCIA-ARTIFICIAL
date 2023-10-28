base_de_conocimiento = {
    "P": True,
    "P => Q": True,
}

# Regla de inferencia: Modus Ponens
if base_de_conocimiento["P"] and base_de_conocimiento["P => Q"]:
    Q = True
    print("Por Modus Ponens, Q es verdadero.")
else:
    Q = False
    print("No se puede inferir el valor de Q.")
