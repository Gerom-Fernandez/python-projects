# Función que imprime un saludo personalizado
def saludar(nombre):
    print(f"hola, {nombre}")

saludar("juan")  # Llama a la función con el nombre "juan"

# Función que suma dos números y devuelve el resultado
def suma(a, b):
    resultado = a + b
    return resultado

# Solicita dos números al usuario y muestra la suma
numero1 = int(input("Introduce un número: "))
numero2 = int(input("Introduce el segundo número: "))
resultado = suma(numero1, numero2)
print(resultado)

# Función que verifica si un número es par
def espar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

# Solicita un número y muestra si es par o no
numero = int(input("Introduce un número: "))
if espar(numero):
    print(f"{numero} es un número par")
else:
    print(f"{numero} no es par")

# Función que devuelve el valor máximo de una lista
def listanumero(lista):
    maximo = max(lista)
    return maximo

# Lista de números y llamada a la función
numeros = [10, 40, 50, 5, 6]
valor = listanumero(numeros)
print("El valor máximo es", valor)

# Función principal que realiza una operación matemática según la elección del usuario
def operacion(operacion_elegida, a, b):
    if operacion_elegida == "sumar":
        resultado = suma(a, b)
    elif operacion_elegida == "restar":
        resultado = restar(a, b)
    elif operacion_elegida == "multiplicar":
        resultado = multiplicar(a, b)
    elif operacion_elegida == "dividir":
        resultado = dividir(a, b)
    else:
        resultado = "Operación no válida"
    return resultado

# Funciones matemáticas básicas
def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "No se puede dividir por cero"

# Interacción con el usuario para realizar una operación
operacion_elegida = input("Elige una operación (sumar, restar, multiplicar o dividir): ")
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))
resultado = operacion(operacion_elegida, numero1, numero2)
print(f"El resultado de la operación es: {resultado}")
