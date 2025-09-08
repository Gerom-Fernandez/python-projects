# Este script muestra cómo se utilizan los diccionarios en Python
# y cómo se puede acceder a sus valores mediante claves.

# Se define un diccionario llamado 'persona' con información básica
persona = {
    "nombre": "juan",
    "edad": 30,
    "ciudad": "Madrid"
}

# Se asigna el diccionario 'persona' a la variable 'perfil'
# Esto no crea una copia, sino que ambas variables apuntan al mismo diccionario
perfil = persona

# Se imprime el valor asociado a la clave 'nombre' dentro del diccionario 'perfil'
print(perfil["nombre"])  # Salida: juan