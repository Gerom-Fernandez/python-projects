# Paso 1
def calculadora(num1, num2, operacion):
    if operacion == "+":
        return num1 + num2
    elif operacion == "-":
        return num1 - num2
    elif operacion == "*":
        return num1 * num2
    elif operacion == "/":
        if num2 == 0:
            return "Error: No se puede dividir por cero."
        return num1 / num2
    else:
        return "Operación no válida."

# Paso 2
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
operacion = input("Ingresa la operación (+, -, * o /): ")

# Paso 3
resultado = calculadora(num1, num2, operacion)
print("Resultado:", resultado)