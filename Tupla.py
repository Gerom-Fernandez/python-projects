# Tupla con números enteros
mi_tupla1 = (1, 2, 3)

# Tupla con cadenas de texto
mi_tupla2 = ("manzana", "banana", "cereza")

# Tupla mixta con diferentes tipos de datos
mi_tupla3 = (1, "hola", 3.14)

# Tupla vacía
tupla_vacia = ()

# Acceso a elementos por índice
print(mi_tupla1[1])      # Muestra el segundo número: 2
print(mi_tupla2[2])      # Muestra la tercera fruta: cereza
print(mi_tupla3[0])      # Muestra el primer elemento: 1

# Tupla anidada con pares (nombre, edad)
persona = (("Juan", 25), ("maria", 16), ("Carlos", 20))

# Iteración sobre la tupla para mostrar personas menores de edad
for nombre, edad in persona:
    if edad < 18:
        print(nombre, edad)  # Muestra: maria 16

# Tupla de números
numero = (10, 20, 30, 40, 50)

# Suma de todos los elementos de la tupla
suma = sum(numero)
print("La suma de los números es:", suma)