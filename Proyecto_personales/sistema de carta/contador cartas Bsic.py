x = 0
user_input = ''
contador = 0
cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
while user_input != contador < 12:
    user_input = input("Ingrese las cartas que tienes: ")
    if user_input in cartas_permitidas:
        if user_input == 'J':
            x = x + 10
        elif user_input == 'Q':
            x = x + 10
        elif user_input == 'K':
            x = x + 10
        elif user_input == 'A':
            x = x + 10
        elif user_input == 'Joker':
            x = x + 30
        elif user_input.isdigit() and 2 <= int(user_input) <= 10:
            x = x + int(user_input)
        contador += 1
    else:
        print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
print(f"puntaje {x}.")
