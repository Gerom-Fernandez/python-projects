# ---------------------------------------------------------------------------------------
# Descripción: Ejemplo de dos formas distintas de implementar una calculadora en Python.
#   - calculadora1: Calculadora con estado interno (resultado acumulado).
#   - calculadora2: Calculadora que opera con dos números y devuelve el resultado directo.
# ---------------------------------------------------------------------------------------

# ----------------------------
# Primera versión: calculadora con resultado acumulado
# ----------------------------
class calculadora1: 
    def __init__(self, numero):
        # Se inicializa con un número de partida (estado interno)
        self.resultado = numero

    def sumar(self, numero):
        self.resultado += numero  # Suma el número al resultado acumulado

    def resta(self, numero):
        self.resultado -= numero  # Resta el número al resultado acumulado

    def multiplicar(self, numero):
        self.resultado *= numero  # Multiplica el resultado acumulado

    def dividir(self, numero):
        # Verifica que el divisor no sea cero
        if numero != 0:
            self.resultado /= numero
        else:
            print("ERROR: No se puede dividir por cero.")
    
    def resultado(self):
        # Devuelve el resultado final acumulado
        return self.resultado
    

# Ejemplo de uso de la calculadora1
calculo = calculadora1(0)  # Comienza en 0

calculo.sumar(5)          # 0 + 5 = 5
calculo.multiplicar(4)    # 5 * 4 = 20
calculo.resta(5)          # 20 - 5 = 15
calculo.dividir(2)        # 15 / 2 = 7.5

resultado = calculo.resultado
print("Resultado acumulado:", resultado)


# ----------------------------
# Segunda versión: calculadora con operaciones independientes
# ----------------------------
class calculadora2:
    def suma(self, num1, num2):
        return num1 + num2  # Devuelve la suma de los dos números

    def resta(self, num1, num2):
        return num1 - num2  # Devuelve la resta de los dos números

    def multiplicar(self, num1, num2):
        return num1 * num2  # Devuelve la multiplicación de los dos números

    def division(self, num1, num2):
        if num2 == 0:
            return "Error: No se puede dividir por cero."  # Manejo de error
        return num1 / num2


# Ejemplo de uso de la calculadora2
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

calc = calculadora2()

# Se realizan todas las operaciones con los dos números
result_suma = calc.suma(num1, num2)
result_resta = calc.resta(num1, num2)
result_multiplicacion = calc.multiplicar(num1, num2)
result_division = calc.division(num1, num2)

# Se muestran los resultados
print("Suma: ", result_suma)
print("Resta: ", result_resta)
print("Multiplicación: ", result_multiplicacion)
print("División: ", result_division)
