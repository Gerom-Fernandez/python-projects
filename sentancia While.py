# Bucle while que cuenta desde 1 hasta 59
contador = 1
while contador < 100:  # Corrección: se usa '<' en lugar de '<-'
    print(contador)
    contador += 1
    if contador == 60:  # El bucle se detiene cuando el contador llega a 60
        break

# Cuenta regresiva desde 10 hasta 1
contador = 10
while contador >= 1:
    print(contador)
    contador -= 1
print("¡Feliz año nuevo!")  # Mensaje final

# Suma acumulativa de números positivos ingresados por el usuario
suma = 0
numero = int(input("Ingresa un número para sumar: "))

while numero >= 0:  # El bucle continúa mientras el número sea positivo o cero
    suma += numero
    numero = int(input("para deter el while debes ingresar un numero negativo: "))

print("La suma de los números ingresados es:", suma)