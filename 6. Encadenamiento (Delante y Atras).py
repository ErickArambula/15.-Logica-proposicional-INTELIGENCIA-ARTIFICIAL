# Conocimiento inicial
conocimiento_inicial = {
    "La computadora no enciende": True,
}

# Reglas
reglas = [
    {
        "condiciones": ["El cable de alimentación está conectado"],
        "resultado": "La computadora no enciende"
    },
    {
        "condiciones": ["El interruptor de encendido está en la posición correcta"],
        "resultado": "El cable de alimentación está conectado"
    },
    {
        "condiciones": ["Hay suficiente energía en la batería"],
        "resultado": "El interruptor de encendido está en la posición correcta"
    },
    {
        "condiciones": ["La computadora debería encenderse"],
        "resultado": "Hay suficiente energía en la batería"
    },
]

# Encadenamiento hacia adelante
def encadenamiento_hacia_adelante(knowledge_base, rules):
    while True:
        nueva_informacion = False
        for rule in rules:
            if all(knowledge_base.get(cond, False) for cond in rule["condiciones"]) and not knowledge_base.get(rule["resultado"], False):
                knowledge_base[rule["resultado"]] = True
                nueva_informacion = True
        if not nueva_informacion:
            break

# Encadenamiento hacia atrás
def encadenamiento_hacia_atras(knowledge_base, rules, objetivo):
    if objetivo in knowledge_base and knowledge_base[objetivo]:
        return True
    for rule in rules:
        if rule["resultado"] == objetivo:
            if all(encadenamiento_hacia_atras(knowledge_base, rules, cond) for cond in rule["condiciones"]):
                knowledge_base[objetivo] = True
                return True
    return False

# Realizar el encadenamiento hacia adelante
encadenamiento_hacia_adelante(conocimiento_inicial, reglas)

# Realizar el encadenamiento hacia atrás
objetivo = "La computadora debería encenderse"
resultado = encadenamiento_hacia_atras(conocimiento_inicial, reglas, objetivo)

# Imprimir el resultado
if resultado:
    print("La computadora debería encenderse.")
else:
    print("No se puede determinar si la computadora debería encenderse.")
