# Definición de la base de conocimiento
base_de_conocimiento = {
    "Rey_en_jaque": True,
    "Turno_de_blancas": True,
    "Torre_blanca_en_jaque": False,
    "Peon_negro_en_jaque": False,
}

# Consulta en la base de conocimiento
if base_de_conocimiento["Rey_en_jaque"]:
    print("El rey está en jaque.")
else:
    print("El rey no está en jaque.")

if base_de_conocimiento["Turno_de_blancas"]:
    print("Es el turno de las blancas.")
else:
    print("Es el turno de las negras.")
