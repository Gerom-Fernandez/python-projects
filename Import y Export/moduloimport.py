# Importa las funciones desde el módulo 'modulosexport'
import modulosexport

# Solicita al usuario que elija una operación
operacion = input("Elige la operación (sumar, restar o multiplicar): ")

# Solicita dos números al usuario
numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

# Ejecuta la operación elegida usando las funciones importadas
if operacion == "sumar":
    resultado = modulosexport.sumar(numero1, numero2)
elif operacion == "restar":
    resultado = modulosexport.resta(numero1, numero2)
elif operacion == "multiplicar":
    resultado = modulosexport.multiplicar(numero1, numero2)
else:
    resultado = "Operación no válida"

# Muestra el resultado
print("El resultado es:", resultado)