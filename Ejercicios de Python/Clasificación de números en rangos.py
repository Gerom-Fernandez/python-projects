num = int(input("Ingresa un número entero: "))

match num:
    case _ if num < 0:
        print("Rango 1: El número es negativo.")
    case _ if 0 <= num < 10:
        print("Rango 2: El número está entre 0 (incluido) y 10 (excluido).")
    case _ if num >= 10:
        print("Rango 3: El número es mayor o igual a 10.")