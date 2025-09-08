# Lista de números
numero = [1, 2, 3, 4, 5]

# Lista de cadenas de texto
frutas = ["manzana", "banna", "cereza"]

# Lista mixta con diferentes tipos de datos
mixata = [1, "hola", 3.14, True]

# Acceso a elementos por índice
print(numero[2])      # Muestra el tercer número: 3
print(frutas[1])      # Muestra la segunda fruta: banna

# Modificación de un elemento en la lista 'numero'
numero[2] = 9
print(numero[2])      # Muestra el nuevo valor: 9

# Agregar un nuevo elemento al final de la lista
numero.append(8)
print(numero)         # Muestra la lista actualizada

# Agregar una nueva fruta
frutas.append("coco")
print(frutas)         # Muestra la lista actualizada

# Eliminar elementos por índice
del numero[2]         # Elimina el tercer elemento (índice 2)
print(numero)

del frutas[0]         # Elimina la primera fruta
print(frutas)

# Recorrer la lista de frutas con un bucle for
for fruta in frutas:
    print(fruta)

# Sumar todos los elementos de la lista 'numero'
suma = sum(numero)
print(suma)

# Otra lista de ejemplo: colores
colores = ["verde", "rojo", "amarillo"]

# Recorrer la lista de colores
for color in colores:
    print(color)