# Lista de frutas
frutas = ["manzana", "banana", "cereza", "naranaja"]
contador = 0 

# Bucle for que recorre cada elemento de la lista 'frutas'
for fruta in frutas:
    contador += 1  # Incrementa el contador en cada iteración
    print(f"fruta {contador}: {fruta}")  # Muestra el número y nombre de la fruta
    if fruta == "banana":  # Si la fruta es 'banana', se detiene el bucle
        break

# Lista de números
numero = [1, 2, 3, 4, 5]

# Bucle for que recorre cada número en la lista
for numeros in numero:
    cuadrado = numeros ** 2  # Calcula el cuadrado del número
    print(f"El cuadrado de {numeros} es {cuadrado}")  # Muestra el resultado