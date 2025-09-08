# Este script muestra cómo funcionan los diccionarios anidados en Python
# y cómo se pueden acceder y modificar sus valores.

# Diccionario que contiene otros diccionarios como valores
persona = {
    "persona1": {
        "nombre": "juan",
        "edad": 30,
        "ciudad": "Madrid"
    },
    "persona2": {
        "nombre": "maria",
        "edad": 28,
        "ciudad": "Barcelona"
    },
    "persona3": {
        "nombre": "carlos",
        "edad": 35,
        "ciudad": "Valencia"
    }
}

# Acceso a los datos de 'persona1' y 'persona2'
datos = persona["persona1"]
datos2 = persona["persona2"]

# Imprime todo el diccionario de 'persona1'
print(datos)

# Imprime solo el nombre de 'persona2'
print(datos2["nombre"])

# Diccionario vacío con claves predefinidas para ingresar datos por teclado
perona1 = {
    "nombre": None,
    "edad": None,
    "dirección": None,
    "telefono": None,
}

# Solicita al usuario que ingrese los datos
perona1["nombre"] = input("Introduzca un nombre: ")
perona1["edad"] = input("Introduzca la edad: ")
perona1["dirección"] = input("Introduzca dirección: ")
perona1["telefono"] = input("Introduzca tu teléfono: ")

# Muestra los datos ingresados en una frase
print(perona1["nombre"], "tiene", perona1["edad"], "años, vive en", perona1["dirección"], "y su teléfono es", perona1["telefono"])