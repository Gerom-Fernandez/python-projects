# main.py
from modulo_personalizado import es_par

# Solicitar al usuario un número
num = int(input("Ingresa un número entero: "))

# Usar la función es_par para verificar
if es_par(num):
    print(f"El número {num} es par.")
else:
    print(f"El número {num} es impar.")