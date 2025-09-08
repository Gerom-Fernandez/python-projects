# Paso 1
datos_personales = {
    "nombre": None,
    "edad": None,
    "direccion": None,
    "telefono": None
}

# Paso 2
datos_personales["nombre"] = input("Ingresa tu nombre: ")
datos_personales["edad"] = input("Ingresa tu edad: ")
datos_personales["direccion"] = input("Ingresa tu dirección: ")
datos_personales["telefono"] = input("Ingresa tu número de teléfono: ")

# Paso 3
print("Datos personales ingresados:")
print("Nombre:", datos_personales["nombre"])
print("Edad:", datos_personales["edad"])
print("Dirección:", datos_personales["direccion"])
print("Teléfono:", datos_personales["telefono"])