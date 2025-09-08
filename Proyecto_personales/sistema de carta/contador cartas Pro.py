'''
El juego de cartas Carioca se puede jugar con un máximo de 8 jugadores1. 
Sin embargo, el juego es idealmente para 4 jugadores. 
Mientras más jugadores participen, la dificultad de armar el juego deseado crece

Dos tríos (6 cartas)
Una escala y un trío (7 cartas)
Dos escalas (8 cartas)
Tres tríos (9 cartas)
Dos tríos y una escala (10 cartas)
Dos escalas y un trío (11 cartas)
Tres escalas (12 cartas)
Cuatro tríos (12 cartas)
Escalera Sucia (13 cartas): Una escala del As al Rey sin importar el color o la pinta.
Escalera Real (13 cartas): Una escala del As al Rey de la misma pinta

'''
jugadoes = int(input('El maximo de jugadores son 8 cuanto van a jugar: '))

if jugadoes == 2:

    jugador_1 = input('Ingresa el nombre del jugadore 1: ')
    jugador_2 = input('Ingresa el nombre del jugadore 2: ')

    print('Primera ronda: Dos tríos')

    # Jugador 1
    x1_total = 0
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2_total = 0
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    print('Segunda ronda: Una escala y un trío')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")


    print('Trecera ronda: Dos escalas')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    print('Cuarta ronda: Tres tríos')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    print('Quinta ronda: Dos tríos y una escala')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    print('Sexta ronda: Dos escalas y un trío')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    print('Septima ronda: Tres escalas')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    print('Octava ronda: Cuatro tríos')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    print('Novena ronda: Escalera Sucia')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    N = input('Quieren hacer la Escala Real (SI o NO): ')
    if N == 'SI':
        print('Decima ronda: Escalera Real')
        # Jugador 1
        x1 = 0
        contador = 0
        cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
        user_input = ''
        while user_input != contador < 12:
            user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
            if user_input in cartas_permitidas:
                if user_input == 'J':
                    x1 = x1 + 10
                elif user_input == 'Q':
                    x1 = x1 + 10
                elif user_input == 'K':
                    x1 = x1 + 10
                elif user_input == 'A':
                    x1 = x1 + 10
                elif user_input == 'Joker':
                    x1 = x1 + 30
                elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                    x1 = x1 + int(user_input)
                contador += 1
            else:
                print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
        x1_total += x1
        print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

        # Jugador 2
        x2 = 0
        contador = 0
        cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
        user_input = ''
        while user_input != contador < 12:
            user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
            if user_input in cartas_permitidas:
                if user_input == 'J':
                    x2 = x2 + 10
                elif user_input == 'Q':
                    x2 = x2 + 10
                elif user_input == 'K':
                    x2 = x2 + 10
                elif user_input == 'A':
                    x2 = x2 + 10
                elif user_input == 'Joker':
                    x2 = x2 + 30
                elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                    x2 = x2 + int(user_input)
                contador += 1
            else:
                print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
        x2_total += x2
        print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    else:
        print('Resultados')
        print(f"Puntaje de {jugador_1} es {x1_total}")
        print(f"Puntaje de {jugador_2} es {x2_total}")

#3
elif jugadoes == 3:
    
    jugador_1 = input('Ingresa el nombre del jugadore 1: ')
    jugador_2 = input('Ingresa el nombre del jugadore 2: ')
    jugador_3 = input('Ingresa el nombre del jugadore 3: ')

    print('Primera ronda: Dos tríos')

    # Jugador 1
    x1_total = 0
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2_total = 0
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # Jugador 3
    x3_total = 0
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    print('Segunda ronda: Una escala y un trío')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # jugador 3
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")


    print('Trecera ronda: Dos escalas')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # jugador 3
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    print('Cuarta ronda: Tres tríos')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # jugador 3
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    print('Quinta ronda: Dos tríos y una escala')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # jugador 3
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    print('Sexta ronda: Dos escalas y un trío')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # jugador 3
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    print('Septima ronda: Tres escalas')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # jugador 3
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    print('Octava ronda: Cuatro tríos')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # jugador 3
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    print('Novena ronda: Escalera Sucia')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # jugador 3
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    N = input('Quieren hacer la Escala Real (SI o NO): ')
    if N == 'SI':
        print('Decima ronda: Escalera Real')
        # Jugador 1
        x1 = 0
        contador = 0
        cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
        user_input = ''
        while user_input != contador < 12:
            user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
            if user_input in cartas_permitidas:
                if user_input == 'J':
                    x1 = x1 + 10
                elif user_input == 'Q':
                    x1 = x1 + 10
                elif user_input == 'K':
                    x1 = x1 + 10
                elif user_input == 'A':
                    x1 = x1 + 10
                elif user_input == 'Joker':
                    x1 = x1 + 30
                elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                    x1 = x1 + int(user_input)
                contador += 1
            else:
                print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
        x1_total += x1
        print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

        # Jugador 2
        x2 = 0
        contador = 0
        cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
        user_input = ''
        while user_input != contador < 12:
            user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
            if user_input in cartas_permitidas:
                if user_input == 'J':
                    x2 = x2 + 10
                elif user_input == 'Q':
                    x2 = x2 + 10
                elif user_input == 'K':
                    x2 = x2 + 10
                elif user_input == 'A':
                    x2 = x2 + 10
                elif user_input == 'Joker':
                    x2 = x2 + 30
                elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                    x2 = x2 + int(user_input)
                contador += 1
            else:
                print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
        x2_total += x2
        print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

        # jugador 3
        x3 = 0
        contador = 0
        cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
        user_input = ''
        while user_input != contador < 12:
            user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
            if user_input in cartas_permitidas:
                if user_input == 'J':
                    x3 = x3 + 10
                elif user_input == 'Q':
                    x3 = x3 + 10
                elif user_input == 'K':
                    x3 = x3 + 10
                elif user_input == 'A':
                    x3 = x3 + 10
                elif user_input == 'Joker':
                    x3 = x3 + 30
                elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                    x3 = x3 + int(user_input)
                contador += 1
            else:
                print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
        x3_total += x3
        print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    else:
        print('Resultados')
        print(f"Puntaje de {jugador_1} es {x1_total}")
        print(f"Puntaje de {jugador_2} es {x2_total}")
        print(f"Puntaje de {jugador_3} es {x3_total}")

elif jugadoes == 4:

    jugador_1 = input('Ingresa el nombre del jugadore 1: ')
    jugador_2 = input('Ingresa el nombre del jugadore 2: ')
    jugador_3 = input('Ingresa el nombre del jugadore 3: ')
    jugador_4 = input('Ingresa el nombre del jugadore 4: ')

    print('Primera ronda: Dos tríos')

    # Jugador 1
    x1_total = 0
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2_total = 0
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # Jugador 3
    x3_total = 0
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    # Jugador 4
    x4_total = 0
    x4 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x4 = x4 + 10
            elif user_input == 'Q':
                x4 = x4 + 10
            elif user_input == 'K':
                x4 = x4 + 10
            elif user_input == 'A':
                x4 = x4 + 10
            elif user_input == 'Joker':
                x4 = x4 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x4 = x4 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x4_total += x4
    print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")


    print('Segunda ronda: Una escala y un trío')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # jugador 3
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    # Jugador 4
    x4 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x4 = x4 + 10
            elif user_input == 'Q':
                x4 = x4 + 10
            elif user_input == 'K':
                x4 = x4 + 10
            elif user_input == 'A':
                x4 = x4 + 10
            elif user_input == 'Joker':
                x4 = x4 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x4 = x4 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x4_total += x4
    print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")


    print('Trecera ronda: Dos escalas')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # jugador 3
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    # Jugador 4
    x4 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x4 = x4 + 10
            elif user_input == 'Q':
                x4 = x4 + 10
            elif user_input == 'K':
                x4 = x4 + 10
            elif user_input == 'A':
                x4 = x4 + 10
            elif user_input == 'Joker':
                x4 = x4 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x4 = x4 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x4_total += x4
    print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")

    print('Cuarta ronda: Tres tríos')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # jugador 3
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    # Jugador 4
    x4 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x4 = x4 + 10
            elif user_input == 'Q':
                x4 = x4 + 10
            elif user_input == 'K':
                x4 = x4 + 10
            elif user_input == 'A':
                x4 = x4 + 10
            elif user_input == 'Joker':
                x4 = x4 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x4 = x4 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x4
    print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")


    print('Quinta ronda: Dos tríos y una escala')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # jugador 3
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    # Jugador 4
    x4 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x4 = x4 + 10
            elif user_input == 'Q':
                x4 = x4 + 10
            elif user_input == 'K':
                x4 = x4 + 10
            elif user_input == 'A':
                x4 = x4 + 10
            elif user_input == 'Joker':
                x4 = x4 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x4 = x4 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x4_total += x4
    print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")


    print('Sexta ronda: Dos escalas y un trío')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # jugador 3
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    # Jugador 4
    x4 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x4 = x4 + 10
            elif user_input == 'Q':
                x4 = x4 + 10
            elif user_input == 'K':
                x4 = x4 + 10
            elif user_input == 'A':
                x4 = x4 + 10
            elif user_input == 'Joker':
                x4 = x4 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x4 = x4 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x4_total += x4
    print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")

    print('Septima ronda: Tres escalas')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # jugador 3
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    # Jugador 4
    x4 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x4 = x4 + 10
            elif user_input == 'Q':
                x4 = x4 + 10
            elif user_input == 'K':
                x4 = x4 + 10
            elif user_input == 'A':
                x4 = x4 + 10
            elif user_input == 'Joker':
                x4 = x4 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x4 = x4 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x4
    print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")


    print('Octava ronda: Cuatro tríos')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # jugador 3
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    # Jugador 4
    x4 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x4 = x4 + 10
            elif user_input == 'Q':
                x4 = x4 + 10
            elif user_input == 'K':
                x4 = x4 + 10
            elif user_input == 'A':
                x4 = x4 + 10
            elif user_input == 'Joker':
                x4 = x4 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x4 = x4 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x4_total += x4
    print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")


    print('Novena ronda: Escalera Sucia')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # jugador 3
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    # Jugador 4
    x4 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x4 = x4 + 10
            elif user_input == 'Q':
                x4 = x4 + 10
            elif user_input == 'K':
                x4 = x4 + 10
            elif user_input == 'A':
                x4 = x4 + 10
            elif user_input == 'Joker':
                x4 = x4 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x4 = x4 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x4_total += x4
    print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")


    N = input('Quieren hacer la Escala Real (SI o NO): ')
    if N == 'SI':
        print('Decima ronda: Escalera Real')
        # Jugador 1
        x1 = 0
        contador = 0
        cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
        user_input = ''
        while user_input != contador < 12:
            user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
            if user_input in cartas_permitidas:
                if user_input == 'J':
                    x1 = x1 + 10
                elif user_input == 'Q':
                    x1 = x1 + 10
                elif user_input == 'K':
                    x1 = x1 + 10
                elif user_input == 'A':
                    x1 = x1 + 10
                elif user_input == 'Joker':
                    x1 = x1 + 30
                elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                    x1 = x1 + int(user_input)
                contador += 1
            else:
                print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
        x1_total += x1
        print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

        # Jugador 2
        x2 = 0
        contador = 0
        cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
        user_input = ''
        while user_input != contador < 12:
            user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
            if user_input in cartas_permitidas:
                if user_input == 'J':
                    x2 = x2 + 10
                elif user_input == 'Q':
                    x2 = x2 + 10
                elif user_input == 'K':
                    x2 = x2 + 10
                elif user_input == 'A':
                    x2 = x2 + 10
                elif user_input == 'Joker':
                    x2 = x2 + 30
                elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                    x2 = x2 + int(user_input)
                contador += 1
            else:
                print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
        x2_total += x2
        print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

        # jugador 3
        x3 = 0
        contador = 0
        cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
        user_input = ''
        while user_input != contador < 12:
            user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
            if user_input in cartas_permitidas:
                if user_input == 'J':
                    x3 = x3 + 10
                elif user_input == 'Q':
                    x3 = x3 + 10
                elif user_input == 'K':
                    x3 = x3 + 10
                elif user_input == 'A':
                    x3 = x3 + 10
                elif user_input == 'Joker':
                    x3 = x3 + 30
                elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                    x3 = x3 + int(user_input)
                contador += 1
            else:
                print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
        x3_total += x3
        print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

        # Jugador 4
        x4 = 0
        contador = 0
        cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
        user_input = ''
        while user_input != contador < 12:
            user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
            if user_input in cartas_permitidas:
                if user_input == 'J':
                    x4 = x4 + 10
                elif user_input == 'Q':
                    x4 = x4 + 10
                elif user_input == 'K':
                    x4 = x4 + 10
                elif user_input == 'A':
                    x4 = x4 + 10
                elif user_input == 'Joker':
                    x4 = x4 + 30
                elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                    x4 = x4 + int(user_input)
                contador += 1
            else:
                print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
        x4_total += x4
        print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")


    else:
        print('Resultados')
        print(f"Puntaje de {jugador_1} es {x1_total}")
        print(f"Puntaje de {jugador_2} es {x2_total}")
        print(f"Puntaje de {jugador_3} es {x3_total}")
        print(f"Puntaje de {jugador_4} es {x4_total}")
    

elif jugadoes == 5:

    jugador_1 = input('Ingresa el nombre del jugadore 1: ')
    jugador_2 = input('Ingresa el nombre del jugadore 2: ')
    jugador_3 = input('Ingresa el nombre del jugadore 3: ')
    jugador_4 = input('Ingresa el nombre del jugadore 4: ')
    jugador_5 = input('Ingresa el nombre del jugadore 5: ')

    print('Primera ronda: Dos tríos')

    # Jugador 1
    x1_total = 0
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2_total = 0
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # Jugador 3
    x3_total = 0
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    # Jugador 4
    x4_total = 0
    x4 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x4 = x4 + 10
            elif user_input == 'Q':
                x4 = x4 + 10
            elif user_input == 'K':
                x4 = x4 + 10
            elif user_input == 'A':
                x4 = x4 + 10
            elif user_input == 'Joker':
                x4 = x4 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x4 = x4 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x4_total += x4
    print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")

    # Jugador 5
    x5_total = 0
    x5 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_5}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x5 = x5 + 10
            elif user_input == 'Q':
                x5 = x5 + 10
            elif user_input == 'K':
                x5 = x5 + 10
            elif user_input == 'A':
                x5 = x5 + 10
            elif user_input == 'Joker':
                x5 = x5 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x5 = x5 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x5_total += x5
    print(f"Puntaje de {jugador_5} en la Primera ronda: {x5}.")



    print('Segunda ronda: Una escala y un trío')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # jugador 3
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    # Jugador 4
    x4 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x4 = x4 + 10
            elif user_input == 'Q':
                x4 = x4 + 10
            elif user_input == 'K':
                x4 = x4 + 10
            elif user_input == 'A':
                x4 = x4 + 10
            elif user_input == 'Joker':
                x4 = x4 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x4 = x4 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x4_total += x4
    print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")

    # jugador 5
    x5 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_5}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x5 = x5 + 10
            elif user_input == 'Q':
                x5 = x5 + 10
            elif user_input == 'K':
                x5 = x5 + 10
            elif user_input == 'A':
                x5 = x5 + 10
            elif user_input == 'Joker':
                x5 = x5 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x5 = x5 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x5_total += x5
    print(f"Puntaje de {jugador_5} en la Primera ronda: {x5}.")


    print('Trecera ronda: Dos escalas')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # jugador 3
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    # Jugador 4
    x4 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x4 = x4 + 10
            elif user_input == 'Q':
                x4 = x4 + 10
            elif user_input == 'K':
                x4 = x4 + 10
            elif user_input == 'A':
                x4 = x4 + 10
            elif user_input == 'Joker':
                x4 = x4 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x4 = x4 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x4_total += x4
    print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")

    # jugador 5
    x5 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while contador < 12:
        user_input = input(f"{jugador_5}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x5 = x5 + 10
            elif user_input == 'Q':
                x5 = x5 + 10
            elif user_input == 'K':
                x5 = x5 + 10
            elif user_input == 'A':
                x5 = x5 + 10
            elif user_input == 'Joker':
                x5 = x5 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x5 = x5 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x5_total += x5
    print(f"Puntaje de {jugador_5} en la Primera ronda: {x5}.")

    print('Cuarta ronda: Tres tríos')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # jugador 3
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    # Jugador 4
    x4 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x4 = x4 + 10
            elif user_input == 'Q':
                x4 = x4 + 10
            elif user_input == 'K':
                x4 = x4 + 10
            elif user_input == 'A':
                x4 = x4 + 10
            elif user_input == 'Joker':
                x4 = x4 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x4 = x4 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x4_total += x4
    print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")

    # jugador 5
    x5 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while contador < 12:
        user_input = input(f"{jugador_5}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x5 = x5 + 10
            elif user_input == 'Q':
                x5 = x5 + 10
            elif user_input == 'K':
                x5 = x5 + 10
            elif user_input == 'A':
                x5 = x5 + 10
            elif user_input == 'Joker':
                x5 = x5 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x5 = x5 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x5_total += x5
    print(f"Puntaje de {jugador_5} en la Primera ronda: {x5}.")

    print('Quinta ronda: Dos tríos y una escala')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # jugador 3
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    # Jugador 4
    x4 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x4 = x4 + 10
            elif user_input == 'Q':
                x4 = x4 + 10
            elif user_input == 'K':
                x4 = x4 + 10
            elif user_input == 'A':
                x4 = x4 + 10
            elif user_input == 'Joker':
                x4 = x4 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x4 = x4 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x4_total += x4
    print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")

    # jugador 5
    x5 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while contador < 12:
        user_input = input(f"{jugador_5}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x5 = x5 + 10
            elif user_input == 'Q':
                x5 = x5 + 10
            elif user_input == 'K':
                x5 = x5 + 10
            elif user_input == 'A':
                x5 = x5 + 10
            elif user_input == 'Joker':
                x5 = x5 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x5 = x5 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x5_total += x5
    print(f"Puntaje de {jugador_5} en la Primera ronda: {x5}.")


    print('Sexta ronda: Dos escalas y un trío')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # jugador 3
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    # Jugador 4
    x4 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x4 = x4 + 10
            elif user_input == 'Q':
                x4 = x4 + 10
            elif user_input == 'K':
                x4 = x4 + 10
            elif user_input == 'A':
                x4 = x4 + 10
            elif user_input == 'Joker':
                x4 = x4 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x4 = x4 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x4_total += x4
    print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")

    # jugador 5
    x5 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while contador < 12:
        user_input = input(f"{jugador_5}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x5 = x5 + 10
            elif user_input == 'Q':
                x5 = x5 + 10
            elif user_input == 'K':
                x5 = x5 + 10
            elif user_input == 'A':
                x5 = x5 + 10
            elif user_input == 'Joker':
                x5 = x5 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x5 = x5 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x5_total += x5
    print(f"Puntaje de {jugador_5} en la Primera ronda: {x5}.")

    print('Septima ronda: Tres escalas')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # jugador 3
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    # Jugador 4
    x4 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x4 = x4 + 10
            elif user_input == 'Q':
                x4 = x4 + 10
            elif user_input == 'K':
                x4 = x4 + 10
            elif user_input == 'A':
                x4 = x4 + 10
            elif user_input == 'Joker':
                x4 = x4 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x4 = x4 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x4_total += x4
    print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")

    # jugador 5
    x5 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while contador < 12:
        user_input = input(f"{jugador_5}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x5 = x5 + 10
            elif user_input == 'Q':
                x5 = x5 + 10
            elif user_input == 'K':
                x5 = x5 + 10
            elif user_input == 'A':
                x5 = x5 + 10
            elif user_input == 'Joker':
                x5 = x5 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x5 = x5 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x5_total += x5
    print(f"Puntaje de {jugador_5} en la Primera ronda: {x5}.")


    print('Octava ronda: Cuatro tríos')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # jugador 3
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    # Jugador 4
    x4 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x4 = x4 + 10
            elif user_input == 'Q':
                x4 = x4 + 10
            elif user_input == 'K':
                x4 = x4 + 10
            elif user_input == 'A':
                x4 = x4 + 10
            elif user_input == 'Joker':
                x4 = x4 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x4 = x4 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x4_total += x4
    print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")

    # jugador 5
    x5 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while contador < 12:
        user_input = input(f"{jugador_5}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x5 = x5 + 10
            elif user_input == 'Q':
                x5 = x5 + 10
            elif user_input == 'K':
                x5 = x5 + 10
            elif user_input == 'A':
                x5 = x5 + 10
            elif user_input == 'Joker':
                x5 = x5 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x5 = x5 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x5_total += x5
    print(f"Puntaje de {jugador_5} en la Primera ronda: {x5}.")


    print('Novena ronda: Escalera Sucia')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # jugador 3
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    # Jugador 4
    x4 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x4 = x4 + 10
            elif user_input == 'Q':
                x4 = x4 + 10
            elif user_input == 'K':
                x4 = x4 + 10
            elif user_input == 'A':
                x4 = x4 + 10
            elif user_input == 'Joker':
                x4 = x4 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x4 = x4 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x4_total += x4
    print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")

    # jugador 5
    x5 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while contador < 12:
        user_input = input(f"{jugador_5}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x5 = x5 + 10
            elif user_input == 'Q':
                x5 = x5 + 10
            elif user_input == 'K':
                x5 = x5 + 10
            elif user_input == 'A':
                x5 = x5 + 10
            elif user_input == 'Joker':
                x5 = x5 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x5 = x5 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x5_total += x5
    print(f"Puntaje de {jugador_5} en la Primera ronda: {x5}.")


    N = input('Quieren hacer la Escala Real (SI o NO): ')
    if N == 'SI':
        print('Decima ronda: Escalera Real')
        # Jugador 1
        x1 = 0
        contador = 0
        cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
        user_input = ''
        while user_input != contador < 12:
            user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
            if user_input in cartas_permitidas:
                if user_input == 'J':
                    x1 = x1 + 10
                elif user_input == 'Q':
                    x1 = x1 + 10
                elif user_input == 'K':
                    x1 = x1 + 10
                elif user_input == 'A':
                    x1 = x1 + 10
                elif user_input == 'Joker':
                    x1 = x1 + 30
                elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                    x1 = x1 + int(user_input)
                contador += 1
            else:
                print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
        x1_total += x1
        print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

        # Jugador 2
        x2 = 0
        contador = 0
        cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
        user_input = ''
        while user_input != contador < 12:
            user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
            if user_input in cartas_permitidas:
                if user_input == 'J':
                    x2 = x2 + 10
                elif user_input == 'Q':
                    x2 = x2 + 10
                elif user_input == 'K':
                    x2 = x2 + 10
                elif user_input == 'A':
                    x2 = x2 + 10
                elif user_input == 'Joker':
                    x2 = x2 + 30
                elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                    x2 = x2 + int(user_input)
                contador += 1
            else:
                print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
        x2_total += x2
        print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

        # jugador 3
        x3 = 0
        contador = 0
        cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
        user_input = ''
        while user_input != contador < 12:
            user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
            if user_input in cartas_permitidas:
                if user_input == 'J':
                    x3 = x3 + 10
                elif user_input == 'Q':
                    x3 = x3 + 10
                elif user_input == 'K':
                    x3 = x3 + 10
                elif user_input == 'A':
                    x3 = x3 + 10
                elif user_input == 'Joker':
                    x3 = x3 + 30
                elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                    x3 = x3 + int(user_input)
                contador += 1
            else:
                print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
        x3_total += x3
        print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

        # Jugador 4
        x4 = 0
        contador = 0
        cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
        user_input = ''
        while user_input != contador < 12:
            user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
            if user_input in cartas_permitidas:
                if user_input == 'J':
                    x4 = x4 + 10
                elif user_input == 'Q':
                    x4 = x4 + 10
                elif user_input == 'K':
                    x4 = x4 + 10
                elif user_input == 'A':
                    x4 = x4 + 10
                elif user_input == 'Joker':
                    x4 = x4 + 30
                elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                    x4 = x4 + int(user_input)
                contador += 1
            else:
                print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
        x4_total += x4
        print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")

        # jugador 5
        x5 = 0
        contador = 0
        cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
        while contador < 12:
            user_input = input(f"{jugador_5}, ingrese las cartas que tienes: ")
            if user_input in cartas_permitidas:
                if user_input == 'J':
                    x5 = x5 + 10
                elif user_input == 'Q':
                    x5 = x5 + 10
                elif user_input == 'K':
                    x5 = x5 + 10
                elif user_input == 'A':
                    x5 = x5 + 10
                elif user_input == 'Joker':
                    x5 = x5 + 30
                elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                    x5 = x5 + int(user_input)
                contador += 1
            else:
                print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
        x5_total += x5
        print(f"Puntaje de {jugador_5} en la Primera ronda: {x5}.")


    else:
        print('Resultados')
        print(f"Puntaje de {jugador_1} es {x1_total}")
        print(f"Puntaje de {jugador_2} es {x2_total}")
        print(f"Puntaje de {jugador_3} es {x3_total}")
        print(f"Puntaje de {jugador_4} es {x4_total}")
        print(f"Puntaje de {jugador_5} es {x5_total}")

elif jugadoes == 6:

    jugador_1 = input('Ingresa el nombre del jugadore 1: ')
    jugador_2 = input('Ingresa el nombre del jugadore 2: ')
    jugador_3 = input('Ingresa el nombre del jugadore 3: ')
    jugador_4 = input('Ingresa el nombre del jugadore 4: ')
    jugador_5 = input('Ingresa el nombre del jugadore 5: ')
    jugador_6 = input('Ingresa el nombre del jugadore 6: ')

    print('Primera ronda: Dos tríos')

    # Jugador 1
    x1_total = 0
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2_total = 0
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # Jugador 3
    x3_total = 0
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    # Jugador 4
    x4_total = 0
    x4 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x4 = x4 + 10
            elif user_input == 'Q':
                x4 = x4 + 10
            elif user_input == 'K':
                x4 = x4 + 10
            elif user_input == 'A':
                x4 = x4 + 10
            elif user_input == 'Joker':
                x4 = x4 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x4 = x4 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x4_total += x4
    print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")

    # Jugador 5
    x5_total = 0
    x5 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_5}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x5 = x5 + 10
            elif user_input == 'Q':
                x5 = x5 + 10
            elif user_input == 'K':
                x5 = x5 + 10
            elif user_input == 'A':
                x5 = x5 + 10
            elif user_input == 'Joker':
                x5 = x5 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x5 = x5 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x5_total += x5
    print(f"Puntaje de {jugador_5} en la Primera ronda: {x5}.")

    # Jugador 6
    x6_total = 0
    x6 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_6}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x6 = x6 + 10
            elif user_input == 'Q':
                x6 = x6 + 10
            elif user_input == 'K':
                x6 = x6 + 10
            elif user_input == 'A':
                x6 = x6 + 10
            elif user_input == 'Joker':
                x6 = x6 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x6 = x6 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x6_total += x6
    print(f"Puntaje de {jugador_6} en la Primera ronda: {x6}.")

    print('Segunda ronda: Una escala y un trío')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # jugador 3
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    # Jugador 4
    x4 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x4 = x4 + 10
            elif user_input == 'Q':
                x4 = x4 + 10
            elif user_input == 'K':
                x4 = x4 + 10
            elif user_input == 'A':
                x4 = x4 + 10
            elif user_input == 'Joker':
                x4 = x4 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x4 = x4 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x4_total += x4
    print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")

    # jugador 5
    x5 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_5}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x5 = x5 + 10
            elif user_input == 'Q':
                x5 = x5 + 10
            elif user_input == 'K':
                x5 = x5 + 10
            elif user_input == 'A':
                x5 = x5 + 10
            elif user_input == 'Joker':
                x5 = x5 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x5 = x5 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x5_total += x5
    print(f"Puntaje de {jugador_5} en la Primera ronda: {x5}.")

    # jugador 6
    x6 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_6}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x6 = x6 + 10
            elif user_input == 'Q':
                x6 = x6 + 10
            elif user_input == 'K':
                x6 = x6 + 10
            elif user_input == 'A':
                x6 = x6 + 10
            elif user_input == 'Joker':
                x6 = x6 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x6 = x6 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x6_total += x6
    print(f"Puntaje de {jugador_6} en la Primera ronda: {x6}.")


    print('Trecera ronda: Dos escalas')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # jugador 3
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    # Jugador 4
    x4 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x4 = x4 + 10
            elif user_input == 'Q':
                x4 = x4 + 10
            elif user_input == 'K':
                x4 = x4 + 10
            elif user_input == 'A':
                x4 = x4 + 10
            elif user_input == 'Joker':
                x4 = x4 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x4 = x4 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x4_total += x4
    print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")

    # jugador 5
    x5 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while contador < 12:
        user_input = input(f"{jugador_5}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x5 = x5 + 10
            elif user_input == 'Q':
                x5 = x5 + 10
            elif user_input == 'K':
                x5 = x5 + 10
            elif user_input == 'A':
                x5 = x5 + 10
            elif user_input == 'Joker':
                x5 = x5 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x5 = x5 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x5_total += x5
    print(f"Puntaje de {jugador_5} en la Primera ronda: {x5}.")

    # jugador 6
    x6 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_6}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x6 = x6 + 10
            elif user_input == 'Q':
                x6 = x6 + 10
            elif user_input == 'K':
                x6 = x6 + 10
            elif user_input == 'A':
                x6 = x6 + 10
            elif user_input == 'Joker':
                x6 = x6 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x6 = x6 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x6_total += x6
    print(f"Puntaje de {jugador_6} en la Primera ronda: {x6}.")


    print('Cuarta ronda: Tres tríos')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # jugador 3
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    # Jugador 4
    x4 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x4 = x4 + 10
            elif user_input == 'Q':
                x4 = x4 + 10
            elif user_input == 'K':
                x4 = x4 + 10
            elif user_input == 'A':
                x4 = x4 + 10
            elif user_input == 'Joker':
                x4 = x4 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x4 = x4 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x4_total += x4
    print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")

    # jugador 5
    x5 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while contador < 12:
        user_input = input(f"{jugador_5}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x5 = x5 + 10
            elif user_input == 'Q':
                x5 = x5 + 10
            elif user_input == 'K':
                x5 = x5 + 10
            elif user_input == 'A':
                x5 = x5 + 10
            elif user_input == 'Joker':
                x5 = x5 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x5 = x5 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x5_total += x5
    print(f"Puntaje de {jugador_5} en la Primera ronda: {x5}.")

    # jugador 6
    x6 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_6}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x6 = x6 + 10
            elif user_input == 'Q':
                x6 = x6 + 10
            elif user_input == 'K':
                x6 = x6 + 10
            elif user_input == 'A':
                x6 = x6 + 10
            elif user_input == 'Joker':
                x6 = x6 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x6 = x6 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x6_total += x6
    print(f"Puntaje de {jugador_6} en la Primera ronda: {x6}.")


    print('Quinta ronda: Dos tríos y una escala')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # jugador 3
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    # Jugador 4
    x4 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x4 = x4 + 10
            elif user_input == 'Q':
                x4 = x4 + 10
            elif user_input == 'K':
                x4 = x4 + 10
            elif user_input == 'A':
                x4 = x4 + 10
            elif user_input == 'Joker':
                x4 = x4 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x4 = x4 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x4_total += x4
    print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")

    # jugador 5
    x5 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while contador < 12:
        user_input = input(f"{jugador_5}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x5 = x5 + 10
            elif user_input == 'Q':
                x5 = x5 + 10
            elif user_input == 'K':
                x5 = x5 + 10
            elif user_input == 'A':
                x5 = x5 + 10
            elif user_input == 'Joker':
                x5 = x5 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x5 = x5 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x5_total += x5
    print(f"Puntaje de {jugador_5} en la Primera ronda: {x5}.")

    # jugador 6
    x6 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_6}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x6 = x6 + 10
            elif user_input == 'Q':
                x6 = x6 + 10
            elif user_input == 'K':
                x6 = x6 + 10
            elif user_input == 'A':
                x6 = x6 + 10
            elif user_input == 'Joker':
                x6 = x6 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x6 = x6 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x6_total += x6
    print(f"Puntaje de {jugador_6} en la Primera ronda: {x6}.")


    print('Sexta ronda: Dos escalas y un trío')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # jugador 3
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    # Jugador 4
    x4 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x4 = x4 + 10
            elif user_input == 'Q':
                x4 = x4 + 10
            elif user_input == 'K':
                x4 = x4 + 10
            elif user_input == 'A':
                x4 = x4 + 10
            elif user_input == 'Joker':
                x4 = x4 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x4 = x4 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x4_total += x4
    print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")

    # jugador 5
    x5 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while contador < 12:
        user_input = input(f"{jugador_5}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x5 = x5 + 10
            elif user_input == 'Q':
                x5 = x5 + 10
            elif user_input == 'K':
                x5 = x5 + 10
            elif user_input == 'A':
                x5 = x5 + 10
            elif user_input == 'Joker':
                x5 = x5 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x5 = x5 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x5_total += x5
    print(f"Puntaje de {jugador_5} en la Primera ronda: {x5}.")

    # jugador 6
    x6 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_6}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x6 = x6 + 10
            elif user_input == 'Q':
                x6 = x6 + 10
            elif user_input == 'K':
                x6 = x6 + 10
            elif user_input == 'A':
                x6 = x6 + 10
            elif user_input == 'Joker':
                x6 = x6 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x6 = x6 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x6_total += x6
    print(f"Puntaje de {jugador_6} en la Primera ronda: {x6}.")


    print('Septima ronda: Tres escalas')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # jugador 3
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    # Jugador 4
    x4 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x4 = x4 + 10
            elif user_input == 'Q':
                x4 = x4 + 10
            elif user_input == 'K':
                x4 = x4 + 10
            elif user_input == 'A':
                x4 = x4 + 10
            elif user_input == 'Joker':
                x4 = x4 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x4 = x4 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x4_total += x4
    print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")

    # jugador 5
    x5 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while contador < 12:
        user_input = input(f"{jugador_5}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x5 = x5 + 10
            elif user_input == 'Q':
                x5 = x5 + 10
            elif user_input == 'K':
                x5 = x5 + 10
            elif user_input == 'A':
                x5 = x5 + 10
            elif user_input == 'Joker':
                x5 = x5 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x5 = x5 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x5_total += x5
    print(f"Puntaje de {jugador_5} en la Primera ronda: {x5}.")

    # jugador 6
    x6 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_6}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x6 = x6 + 10
            elif user_input == 'Q':
                x6 = x6 + 10
            elif user_input == 'K':
                x6 = x6 + 10
            elif user_input == 'A':
                x6 = x6 + 10
            elif user_input == 'Joker':
                x6 = x6 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x6 = x6 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x6_total += x6
    print(f"Puntaje de {jugador_6} en la Primera ronda: {x6}.")


    print('Octava ronda: Cuatro tríos')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # jugador 3
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    # Jugador 4
    x4 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x4 = x4 + 10
            elif user_input == 'Q':
                x4 = x4 + 10
            elif user_input == 'K':
                x4 = x4 + 10
            elif user_input == 'A':
                x4 = x4 + 10
            elif user_input == 'Joker':
                x4 = x4 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x4 = x4 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x4_total += x4
    print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")

    # jugador 5
    x5 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while contador < 12:
        user_input = input(f"{jugador_5}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x5 = x5 + 10
            elif user_input == 'Q':
                x5 = x5 + 10
            elif user_input == 'K':
                x5 = x5 + 10
            elif user_input == 'A':
                x5 = x5 + 10
            elif user_input == 'Joker':
                x5 = x5 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x5 = x5 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x5_total += x5
    print(f"Puntaje de {jugador_5} en la Primera ronda: {x5}.")

    # jugador 6
    x6 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_6}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x6 = x6 + 10
            elif user_input == 'Q':
                x6 = x6 + 10
            elif user_input == 'K':
                x6 = x6 + 10
            elif user_input == 'A':
                x6 = x6 + 10
            elif user_input == 'Joker':
                x6 = x6 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x6 = x6 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x6_total += x6
    print(f"Puntaje de {jugador_6} en la Primera ronda: {x6}.")


    print('Novena ronda: Escalera Sucia')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # jugador 3
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    # Jugador 4
    x4 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x4 = x4 + 10
            elif user_input == 'Q':
                x4 = x4 + 10
            elif user_input == 'K':
                x4 = x4 + 10
            elif user_input == 'A':
                x4 = x4 + 10
            elif user_input == 'Joker':
                x4 = x4 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x4 = x4 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x4_total += x4
    print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")

    # jugador 5
    x5 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while contador < 12:
        user_input = input(f"{jugador_5}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x5 = x5 + 10
            elif user_input == 'Q':
                x5 = x5 + 10
            elif user_input == 'K':
                x5 = x5 + 10
            elif user_input == 'A':
                x5 = x5 + 10
            elif user_input == 'Joker':
                x5 = x5 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x5 = x5 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x5_total += x5
    print(f"Puntaje de {jugador_5} en la Primera ronda: {x5}.")

    # jugador 6
    x6 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_6}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x6 = x6 + 10
            elif user_input == 'Q':
                x6 = x6 + 10
            elif user_input == 'K':
                x6 = x6 + 10
            elif user_input == 'A':
                x6 = x6 + 10
            elif user_input == 'Joker':
                x6 = x6 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x6 = x6 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x6_total += x6
    print(f"Puntaje de {jugador_6} en la Primera ronda: {x6}.")


    N = input('Quieren hacer la Escala Real (SI o NO): ')
    if N == 'SI':
        print('Decima ronda: Escalera Real')
        # Jugador 1
        x1 = 0
        contador = 0
        cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
        user_input = ''
        while user_input != contador < 12:
            user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
            if user_input in cartas_permitidas:
                if user_input == 'J':
                    x1 = x1 + 10
                elif user_input == 'Q':
                    x1 = x1 + 10
                elif user_input == 'K':
                    x1 = x1 + 10
                elif user_input == 'A':
                    x1 = x1 + 10
                elif user_input == 'Joker':
                    x1 = x1 + 30
                elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                    x1 = x1 + int(user_input)
                contador += 1
            else:
                print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
        x1_total += x1
        print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

        # Jugador 2
        x2 = 0
        contador = 0
        cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
        user_input = ''
        while user_input != contador < 12:
            user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
            if user_input in cartas_permitidas:
                if user_input == 'J':
                    x2 = x2 + 10
                elif user_input == 'Q':
                    x2 = x2 + 10
                elif user_input == 'K':
                    x2 = x2 + 10
                elif user_input == 'A':
                    x2 = x2 + 10
                elif user_input == 'Joker':
                    x2 = x2 + 30
                elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                    x2 = x2 + int(user_input)
                contador += 1
            else:
                print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
        x2_total += x2
        print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

        # jugador 3
        x3 = 0
        contador = 0
        cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
        user_input = ''
        while user_input != contador < 12:
            user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
            if user_input in cartas_permitidas:
                if user_input == 'J':
                    x3 = x3 + 10
                elif user_input == 'Q':
                    x3 = x3 + 10
                elif user_input == 'K':
                    x3 = x3 + 10
                elif user_input == 'A':
                    x3 = x3 + 10
                elif user_input == 'Joker':
                    x3 = x3 + 30
                elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                    x3 = x3 + int(user_input)
                contador += 1
            else:
                print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
        x3_total += x3
        print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

        # Jugador 4
        x4 = 0
        contador = 0
        cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
        user_input = ''
        while user_input != contador < 12:
            user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
            if user_input in cartas_permitidas:
                if user_input == 'J':
                    x4 = x4 + 10
                elif user_input == 'Q':
                    x4 = x4 + 10
                elif user_input == 'K':
                    x4 = x4 + 10
                elif user_input == 'A':
                    x4 = x4 + 10
                elif user_input == 'Joker':
                    x4 = x4 + 30
                elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                    x4 = x4 + int(user_input)
                contador += 1
            else:
                print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
        x4_total += x4
        print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")

        # jugador 5
        x5 = 0
        contador = 0
        cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
        while contador < 12:
            user_input = input(f"{jugador_5}, ingrese las cartas que tienes: ")
            if user_input in cartas_permitidas:
                if user_input == 'J':
                    x5 = x5 + 10
                elif user_input == 'Q':
                    x5 = x5 + 10
                elif user_input == 'K':
                    x5 = x5 + 10
                elif user_input == 'A':
                    x5 = x5 + 10
                elif user_input == 'Joker':
                    x5 = x5 + 30
                elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                    x5 = x5 + int(user_input)
                contador += 1
            else:
                print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
        x5_total += x5
        print(f"Puntaje de {jugador_5} en la Primera ronda: {x5}.")

        # jugador 6
        x6 = 0
        contador = 0
        cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
        while user_input != contador < 12:
            user_input = input(f"{jugador_6}, ingrese las cartas que tienes: ")
            if user_input in cartas_permitidas:
                if user_input == 'J':
                    x6 = x6 + 10
                elif user_input == 'Q':
                    x6 = x6 + 10
                elif user_input == 'K':
                    x6 = x6 + 10
                elif user_input == 'A':
                    x6 = x6 + 10
                elif user_input == 'Joker':
                    x6 = x6 + 30
                elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                    x6 = x6 + int(user_input)
                contador += 1
            else:
                print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
        x6_total += x6
        print(f"Puntaje de {jugador_6} en la Primera ronda: {x6}.")


    else:
        print('Resultados')
        print(f"Puntaje de {jugador_1} es {x1_total}")
        print(f"Puntaje de {jugador_2} es {x2_total}")
        print(f"Puntaje de {jugador_3} es {x3_total}")
        print(f"Puntaje de {jugador_4} es {x4_total}")
        print(f"Puntaje de {jugador_5} es {x5_total}")
        print(f"Puntaje de {jugador_6} es {x6_total}")

elif jugadoes == 7:

    jugador_1 = input('Ingresa el nombre del jugadore 1: ')
    jugador_2 = input('Ingresa el nombre del jugadore 2: ')
    jugador_3 = input('Ingresa el nombre del jugadore 3: ')
    jugador_4 = input('Ingresa el nombre del jugadore 4: ')
    jugador_5 = input('Ingresa el nombre del jugadore 5: ')
    jugador_6 = input('Ingresa el nombre del jugadore 6: ')
    jugador_7 = input('Ingresa el nombre del jugadore 7: ')

    print('Primera ronda: Dos tríos')

    # Jugador 1
    x1_total = 0
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2_total = 0
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # Jugador 3
    x3_total = 0
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    # Jugador 4
    x4_total = 0
    x4 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x4 = x4 + 10
            elif user_input == 'Q':
                x4 = x4 + 10
            elif user_input == 'K':
                x4 = x4 + 10
            elif user_input == 'A':
                x4 = x4 + 10
            elif user_input == 'Joker':
                x4 = x4 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x4 = x4 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x4_total += x4
    print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")

    # Jugador 5
    x5_total = 0
    x5 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_5}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x5 = x5 + 10
            elif user_input == 'Q':
                x5 = x5 + 10
            elif user_input == 'K':
                x5 = x5 + 10
            elif user_input == 'A':
                x5 = x5 + 10
            elif user_input == 'Joker':
                x5 = x5 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x5 = x5 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x5_total += x5
    print(f"Puntaje de {jugador_5} en la Primera ronda: {x5}.")

    # Jugador 6
    x6_total = 0
    x6 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_6}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x6 = x6 + 10
            elif user_input == 'Q':
                x6 = x6 + 10
            elif user_input == 'K':
                x6 = x6 + 10
            elif user_input == 'A':
                x6 = x6 + 10
            elif user_input == 'Joker':
                x6 = x6 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x6 = x6 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x6_total += x6
    print(f"Puntaje de {jugador_6} en la Primera ronda: {x6}.")

    # Jugador 7
    x7_total = 0
    x7 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_7}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x7 = x7 + 10
            elif user_input == 'Q':
                x7 = x7 + 10
            elif user_input == 'K':
                x7 = x7 + 10
            elif user_input == 'A':
                x7 = x7 + 10
            elif user_input == 'Joker':
                x7 = x7 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x7 = x7 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x7_total += x7
    print(f"Puntaje de {jugador_7} en la Primera ronda: {x7}.")

    print('Segunda ronda: Una escala y un trío')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # jugador 3
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    # Jugador 4
    x4 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x4 = x4 + 10
            elif user_input == 'Q':
                x4 = x4 + 10
            elif user_input == 'K':
                x4 = x4 + 10
            elif user_input == 'A':
                x4 = x4 + 10
            elif user_input == 'Joker':
                x4 = x4 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x4 = x4 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x4_total += x4
    print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")

    # jugador 5
    x5 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_5}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x5 = x5 + 10
            elif user_input == 'Q':
                x5 = x5 + 10
            elif user_input == 'K':
                x5 = x5 + 10
            elif user_input == 'A':
                x5 = x5 + 10
            elif user_input == 'Joker':
                x5 = x5 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x5 = x5 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x5_total += x5
    print(f"Puntaje de {jugador_5} en la Primera ronda: {x5}.")

    # jugador 6
    x6 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_6}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x6 = x6 + 10
            elif user_input == 'Q':
                x6 = x6 + 10
            elif user_input == 'K':
                x6 = x6 + 10
            elif user_input == 'A':
                x6 = x6 + 10
            elif user_input == 'Joker':
                x6 = x6 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x6 = x6 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x6_total += x6
    print(f"Puntaje de {jugador_6} en la Primera ronda: {x6}.")

    # jugador 7
    x7 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_7}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x7 = x7 + 10
            elif user_input == 'Q':
                x7 = x7 + 10
            elif user_input == 'K':
                x7 = x7 + 10
            elif user_input == 'A':
                x7 = x7 + 10
            elif user_input == 'Joker':
                x7 = x7 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x7 = x7 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x7_total += x7
    print(f"Puntaje de {jugador_7} en la Primera ronda: {x7}.")


    print('Trecera ronda: Dos escalas')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # jugador 3
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    # Jugador 4
    x4 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x4 = x4 + 10
            elif user_input == 'Q':
                x4 = x4 + 10
            elif user_input == 'K':
                x4 = x4 + 10
            elif user_input == 'A':
                x4 = x4 + 10
            elif user_input == 'Joker':
                x4 = x4 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x4 = x4 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x4_total += x4
    print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")

    # jugador 5
    x5 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while contador < 12:
        user_input = input(f"{jugador_5}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x5 = x5 + 10
            elif user_input == 'Q':
                x5 = x5 + 10
            elif user_input == 'K':
                x5 = x5 + 10
            elif user_input == 'A':
                x5 = x5 + 10
            elif user_input == 'Joker':
                x5 = x5 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x5 = x5 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x5_total += x5
    print(f"Puntaje de {jugador_5} en la Primera ronda: {x5}.")

    # jugador 6
    x6 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_6}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x6 = x6 + 10
            elif user_input == 'Q':
                x6 = x6 + 10
            elif user_input == 'K':
                x6 = x6 + 10
            elif user_input == 'A':
                x6 = x6 + 10
            elif user_input == 'Joker':
                x6 = x6 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x6 = x6 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x6_total += x6
    print(f"Puntaje de {jugador_6} en la Primera ronda: {x6}.")

    # jugador 7
    x7 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_7}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x7 = x7 + 10
            elif user_input == 'Q':
                x7 = x7 + 10
            elif user_input == 'K':
                x7 = x7 + 10
            elif user_input == 'A':
                x7 = x7 + 10
            elif user_input == 'Joker':
                x7 = x7 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x7 = x7 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x7_total += x7
    print(f"Puntaje de {jugador_7} en la Primera ronda: {x7}.")

    print('Cuarta ronda: Tres tríos')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # jugador 3
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    # Jugador 4
    x4 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x4 = x4 + 10
            elif user_input == 'Q':
                x4 = x4 + 10
            elif user_input == 'K':
                x4 = x4 + 10
            elif user_input == 'A':
                x4 = x4 + 10
            elif user_input == 'Joker':
                x4 = x4 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x4 = x4 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x4_total += x4
    print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")

    # jugador 5
    x5 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while contador < 12:
        user_input = input(f"{jugador_5}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x5 = x5 + 10
            elif user_input == 'Q':
                x5 = x5 + 10
            elif user_input == 'K':
                x5 = x5 + 10
            elif user_input == 'A':
                x5 = x5 + 10
            elif user_input == 'Joker':
                x5 = x5 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x5 = x5 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x5_total += x5
    print(f"Puntaje de {jugador_5} en la Primera ronda: {x5}.")

    # jugador 6
    x6 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_6}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x6 = x6 + 10
            elif user_input == 'Q':
                x6 = x6 + 10
            elif user_input == 'K':
                x6 = x6 + 10
            elif user_input == 'A':
                x6 = x6 + 10
            elif user_input == 'Joker':
                x6 = x6 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x6 = x6 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x6_total += x6
    print(f"Puntaje de {jugador_6} en la Primera ronda: {x6}.")

    # jugador 7
    x7 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_7}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x7 = x7 + 10
            elif user_input == 'Q':
                x7 = x7 + 10
            elif user_input == 'K':
                x7 = x7 + 10
            elif user_input == 'A':
                x7 = x7 + 10
            elif user_input == 'Joker':
                x7 = x7 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x7 = x7 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x7_total += x7
    print(f"Puntaje de {jugador_7} en la Primera ronda: {x7}.")

    print('Quinta ronda: Dos tríos y una escala')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # jugador 3
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    # Jugador 4
    x4 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x4 = x4 + 10
            elif user_input == 'Q':
                x4 = x4 + 10
            elif user_input == 'K':
                x4 = x4 + 10
            elif user_input == 'A':
                x4 = x4 + 10
            elif user_input == 'Joker':
                x4 = x4 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x4 = x4 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x4_total += x4
    print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")

    # jugador 5
    x5 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while contador < 12:
        user_input = input(f"{jugador_5}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x5 = x5 + 10
            elif user_input == 'Q':
                x5 = x5 + 10
            elif user_input == 'K':
                x5 = x5 + 10
            elif user_input == 'A':
                x5 = x5 + 10
            elif user_input == 'Joker':
                x5 = x5 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x5 = x5 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x5_total += x5
    print(f"Puntaje de {jugador_5} en la Primera ronda: {x5}.")

    # jugador 6
    x6 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_6}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x6 = x6 + 10
            elif user_input == 'Q':
                x6 = x6 + 10
            elif user_input == 'K':
                x6 = x6 + 10
            elif user_input == 'A':
                x6 = x6 + 10
            elif user_input == 'Joker':
                x6 = x6 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x6 = x6 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x6_total += x6
    print(f"Puntaje de {jugador_6} en la Primera ronda: {x6}.")

    # jugador 7
    x7 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_7}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x7 = x7 + 10
            elif user_input == 'Q':
                x7 = x7 + 10
            elif user_input == 'K':
                x7 = x7 + 10
            elif user_input == 'A':
                x7 = x7 + 10
            elif user_input == 'Joker':
                x7 = x7 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x7 = x7 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x7_total += x7
    print(f"Puntaje de {jugador_7} en la Primera ronda: {x7}.")

    print('Sexta ronda: Dos escalas y un trío')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # jugador 3
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    # Jugador 4
    x4 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x4 = x4 + 10
            elif user_input == 'Q':
                x4 = x4 + 10
            elif user_input == 'K':
                x4 = x4 + 10
            elif user_input == 'A':
                x4 = x4 + 10
            elif user_input == 'Joker':
                x4 = x4 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x4 = x4 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x4_total += x4
    print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")

    # jugador 5
    x5 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while contador < 12:
        user_input = input(f"{jugador_5}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x5 = x5 + 10
            elif user_input == 'Q':
                x5 = x5 + 10
            elif user_input == 'K':
                x5 = x5 + 10
            elif user_input == 'A':
                x5 = x5 + 10
            elif user_input == 'Joker':
                x5 = x5 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x5 = x5 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x5_total += x5
    print(f"Puntaje de {jugador_5} en la Primera ronda: {x5}.")

    # jugador 6
    x6 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_6}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x6 = x6 + 10
            elif user_input == 'Q':
                x6 = x6 + 10
            elif user_input == 'K':
                x6 = x6 + 10
            elif user_input == 'A':
                x6 = x6 + 10
            elif user_input == 'Joker':
                x6 = x6 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x6 = x6 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x6_total += x6
    print(f"Puntaje de {jugador_6} en la Primera ronda: {x6}.")

    # jugador 7
    x7 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_7}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x7 = x7 + 10
            elif user_input == 'Q':
                x7 = x7 + 10
            elif user_input == 'K':
                x7 = x7 + 10
            elif user_input == 'A':
                x7 = x7 + 10
            elif user_input == 'Joker':
                x7 = x7 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x7 = x7 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x7_total += x7
    print(f"Puntaje de {jugador_7} en la Primera ronda: {x7}.")

    print('Septima ronda: Tres escalas')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # jugador 3
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    # Jugador 4
    x4 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x4 = x4 + 10
            elif user_input == 'Q':
                x4 = x4 + 10
            elif user_input == 'K':
                x4 = x4 + 10
            elif user_input == 'A':
                x4 = x4 + 10
            elif user_input == 'Joker':
                x4 = x4 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x4 = x4 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x4_total += x4
    print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")

    # jugador 5
    x5 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while contador < 12:
        user_input = input(f"{jugador_5}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x5 = x5 + 10
            elif user_input == 'Q':
                x5 = x5 + 10
            elif user_input == 'K':
                x5 = x5 + 10
            elif user_input == 'A':
                x5 = x5 + 10
            elif user_input == 'Joker':
                x5 = x5 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x5 = x5 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x5_total += x5
    print(f"Puntaje de {jugador_5} en la Primera ronda: {x5}.")

    # jugador 6
    x6 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_6}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x6 = x6 + 10
            elif user_input == 'Q':
                x6 = x6 + 10
            elif user_input == 'K':
                x6 = x6 + 10
            elif user_input == 'A':
                x6 = x6 + 10
            elif user_input == 'Joker':
                x6 = x6 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x6 = x6 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x6_total += x6
    print(f"Puntaje de {jugador_6} en la Primera ronda: {x6}.")

    # jugador 7
    x7 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_7}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x7 = x7 + 10
            elif user_input == 'Q':
                x7 = x7 + 10
            elif user_input == 'K':
                x7 = x7 + 10
            elif user_input == 'A':
                x7 = x7 + 10
            elif user_input == 'Joker':
                x7 = x7 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x7 = x7 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x7_total += x7
    print(f"Puntaje de {jugador_7} en la Primera ronda: {x7}.")

    print('Octava ronda: Cuatro tríos')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # jugador 3
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    # Jugador 4
    x4 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x4 = x4 + 10
            elif user_input == 'Q':
                x4 = x4 + 10
            elif user_input == 'K':
                x4 = x4 + 10
            elif user_input == 'A':
                x4 = x4 + 10
            elif user_input == 'Joker':
                x4 = x4 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x4 = x4 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x4_total += x4
    print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")

    # jugador 5
    x5 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while contador < 12:
        user_input = input(f"{jugador_5}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x5 = x5 + 10
            elif user_input == 'Q':
                x5 = x5 + 10
            elif user_input == 'K':
                x5 = x5 + 10
            elif user_input == 'A':
                x5 = x5 + 10
            elif user_input == 'Joker':
                x5 = x5 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x5 = x5 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x5_total += x5
    print(f"Puntaje de {jugador_5} en la Primera ronda: {x5}.")

    # jugador 6
    x6 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_6}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x6 = x6 + 10
            elif user_input == 'Q':
                x6 = x6 + 10
            elif user_input == 'K':
                x6 = x6 + 10
            elif user_input == 'A':
                x6 = x6 + 10
            elif user_input == 'Joker':
                x6 = x6 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x6 = x6 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x6_total += x6
    print(f"Puntaje de {jugador_6} en la Primera ronda: {x6}.")

    # jugador 7
    x7 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_7}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x7 = x7 + 10
            elif user_input == 'Q':
                x7 = x7 + 10
            elif user_input == 'K':
                x7 = x7 + 10
            elif user_input == 'A':
                x7 = x7 + 10
            elif user_input == 'Joker':
                x7 = x7 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x7 = x7 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x7_total += x7
    print(f"Puntaje de {jugador_7} en la Primera ronda: {x7}.")

    print('Novena ronda: Escalera Sucia')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # jugador 3
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    # Jugador 4
    x4 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x4 = x4 + 10
            elif user_input == 'Q':
                x4 = x4 + 10
            elif user_input == 'K':
                x4 = x4 + 10
            elif user_input == 'A':
                x4 = x4 + 10
            elif user_input == 'Joker':
                x4 = x4 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x4 = x4 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x4_total += x4
    print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")

    # jugador 5
    x5 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while contador < 12:
        user_input = input(f"{jugador_5}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x5 = x5 + 10
            elif user_input == 'Q':
                x5 = x5 + 10
            elif user_input == 'K':
                x5 = x5 + 10
            elif user_input == 'A':
                x5 = x5 + 10
            elif user_input == 'Joker':
                x5 = x5 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x5 = x5 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x5_total += x5
    print(f"Puntaje de {jugador_5} en la Primera ronda: {x5}.")

    # jugador 6
    x6 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_6}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x6 = x6 + 10
            elif user_input == 'Q':
                x6 = x6 + 10
            elif user_input == 'K':
                x6 = x6 + 10
            elif user_input == 'A':
                x6 = x6 + 10
            elif user_input == 'Joker':
                x6 = x6 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x6 = x6 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x6_total += x6
    print(f"Puntaje de {jugador_6} en la Primera ronda: {x6}.")

    # jugador 7
    x7 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_7}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x7 = x7 + 10
            elif user_input == 'Q':
                x7 = x7 + 10
            elif user_input == 'K':
                x7 = x7 + 10
            elif user_input == 'A':
                x7 = x7 + 10
            elif user_input == 'Joker':
                x7 = x7 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x7 = x7 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x7_total += x7
    print(f"Puntaje de {jugador_7} en la Primera ronda: {x7}.")

    N = input('Quieren hacer la Escala Real (SI o NO): ')
    if N == 'SI':
        print('Decima ronda: Escalera Real')
        # Jugador 1
        x1 = 0
        contador = 0
        cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
        user_input = ''
        while user_input != contador < 12:
            user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
            if user_input in cartas_permitidas:
                if user_input == 'J':
                    x1 = x1 + 10
                elif user_input == 'Q':
                    x1 = x1 + 10
                elif user_input == 'K':
                    x1 = x1 + 10
                elif user_input == 'A':
                    x1 = x1 + 10
                elif user_input == 'Joker':
                    x1 = x1 + 30
                elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                    x1 = x1 + int(user_input)
                contador += 1
            else:
                print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
        x1_total += x1
        print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

        # Jugador 2
        x2 = 0
        contador = 0
        cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
        user_input = ''
        while user_input != contador < 12:
            user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
            if user_input in cartas_permitidas:
                if user_input == 'J':
                    x2 = x2 + 10
                elif user_input == 'Q':
                    x2 = x2 + 10
                elif user_input == 'K':
                    x2 = x2 + 10
                elif user_input == 'A':
                    x2 = x2 + 10
                elif user_input == 'Joker':
                    x2 = x2 + 30
                elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                    x2 = x2 + int(user_input)
                contador += 1
            else:
                print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
        x2_total += x2
        print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

        # jugador 3
        x3 = 0
        contador = 0
        cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
        user_input = ''
        while user_input != contador < 12:
            user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
            if user_input in cartas_permitidas:
                if user_input == 'J':
                    x3 = x3 + 10
                elif user_input == 'Q':
                    x3 = x3 + 10
                elif user_input == 'K':
                    x3 = x3 + 10
                elif user_input == 'A':
                    x3 = x3 + 10
                elif user_input == 'Joker':
                    x3 = x3 + 30
                elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                    x3 = x3 + int(user_input)
                contador += 1
            else:
                print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
        x3_total += x3
        print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

        # Jugador 4
        x4 = 0
        contador = 0
        cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
        user_input = ''
        while user_input != contador < 12:
            user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
            if user_input in cartas_permitidas:
                if user_input == 'J':
                    x4 = x4 + 10
                elif user_input == 'Q':
                    x4 = x4 + 10
                elif user_input == 'K':
                    x4 = x4 + 10
                elif user_input == 'A':
                    x4 = x4 + 10
                elif user_input == 'Joker':
                    x4 = x4 + 30
                elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                    x4 = x4 + int(user_input)
                contador += 1
            else:
                print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
        x4_total += x4
        print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")

        # jugador 5
        x5 = 0
        contador = 0
        cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
        while contador < 12:
            user_input = input(f"{jugador_5}, ingrese las cartas que tienes: ")
            if user_input in cartas_permitidas:
                if user_input == 'J':
                    x5 = x5 + 10
                elif user_input == 'Q':
                    x5 = x5 + 10
                elif user_input == 'K':
                    x5 = x5 + 10
                elif user_input == 'A':
                    x5 = x5 + 10
                elif user_input == 'Joker':
                    x5 = x5 + 30
                elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                    x5 = x5 + int(user_input)
                contador += 1
            else:
                print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
        x5_total += x5
        print(f"Puntaje de {jugador_5} en la Primera ronda: {x5}.")

        # jugador 6
        x6 = 0
        contador = 0
        cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
        while user_input != contador < 12:
            user_input = input(f"{jugador_6}, ingrese las cartas que tienes: ")
            if user_input in cartas_permitidas:
                if user_input == 'J':
                    x6 = x6 + 10
                elif user_input == 'Q':
                    x6 = x6 + 10
                elif user_input == 'K':
                    x6 = x6 + 10
                elif user_input == 'A':
                    x6 = x6 + 10
                elif user_input == 'Joker':
                    x6 = x6 + 30
                elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                    x6 = x6 + int(user_input)
                contador += 1
            else:
                print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
        x6_total += x6
        print(f"Puntaje de {jugador_6} en la Primera ronda: {x6}.")

        # jugador 7
        x7 = 0
        contador = 0
        cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
        while user_input != contador < 12:
            user_input = input(f"{jugador_7}, ingrese las cartas que tienes: ")
            if user_input in cartas_permitidas:
                if user_input == 'J':
                    x7 = x7 + 10
                elif user_input == 'Q':
                    x7 = x7 + 10
                elif user_input == 'K':
                    x7 = x7 + 10
                elif user_input == 'A':
                    x7 = x7 + 10
                elif user_input == 'Joker':
                    x7 = x7 + 30
                elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                    x7 = x7 + int(user_input)
                contador += 1
            else:
                print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
        x7_total += x7
        print(f"Puntaje de {jugador_7} en la Primera ronda: {x7}.")



    else:
        print('Resultados')
        print(f"Puntaje de {jugador_1} es {x1_total}")
        print(f"Puntaje de {jugador_2} es {x2_total}")
        print(f"Puntaje de {jugador_3} es {x3_total}")
        print(f"Puntaje de {jugador_4} es {x4_total}")
        print(f"Puntaje de {jugador_5} es {x5_total}")
        print(f"Puntaje de {jugador_6} es {x6_total}")
        print(f"Puntaje de {jugador_7} es {x7_total}")

elif jugadoes == 8:

    jugador_1 = input('Ingresa el nombre del jugadore 1: ')
    jugador_2 = input('Ingresa el nombre del jugadore 2: ')
    jugador_3 = input('Ingresa el nombre del jugadore 3: ')
    jugador_4 = input('Ingresa el nombre del jugadore 4: ')
    jugador_5 = input('Ingresa el nombre del jugadore 5: ')
    jugador_6 = input('Ingresa el nombre del jugadore 6: ')
    jugador_7 = input('Ingresa el nombre del jugadore 7: ')
    jugador_8 = input('Ingresa el nombre del jugadore 8: ')

    print('Primera ronda: Dos tríos')

    # Jugador 1
    x1_total = 0
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2_total = 0
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # Jugador 3
    x3_total = 0
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    # Jugador 4
    x4_total = 0
    x4 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x4 = x4 + 10
            elif user_input == 'Q':
                x4 = x4 + 10
            elif user_input == 'K':
                x4 = x4 + 10
            elif user_input == 'A':
                x4 = x4 + 10
            elif user_input == 'Joker':
                x4 = x4 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x4 = x4 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x4_total += x4
    print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")

    # Jugador 5
    x5_total = 0
    x5 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_5}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x5 = x5 + 10
            elif user_input == 'Q':
                x5 = x5 + 10
            elif user_input == 'K':
                x5 = x5 + 10
            elif user_input == 'A':
                x5 = x5 + 10
            elif user_input == 'Joker':
                x5 = x5 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x5 = x5 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x5_total += x5
    print(f"Puntaje de {jugador_5} en la Primera ronda: {x5}.")

    # Jugador 6
    x6_total = 0
    x6 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_6}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x6 = x6 + 10
            elif user_input == 'Q':
                x6 = x6 + 10
            elif user_input == 'K':
                x6 = x6 + 10
            elif user_input == 'A':
                x6 = x6 + 10
            elif user_input == 'Joker':
                x6 = x6 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x6 = x6 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x6_total += x6
    print(f"Puntaje de {jugador_6} en la Primera ronda: {x6}.")

    # Jugador 7
    x7_total = 0
    x7 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_7}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x7 = x7 + 10
            elif user_input == 'Q':
                x7 = x7 + 10
            elif user_input == 'K':
                x7 = x7 + 10
            elif user_input == 'A':
                x7 = x7 + 10
            elif user_input == 'Joker':
                x7 = x7 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x7 = x7 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x7_total += x7
    print(f"Puntaje de {jugador_7} en la Primera ronda: {x7}.")

    # Jugador 8
    x8_total = 0
    x8 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_8}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x8 = x8 + 10
            elif user_input == 'Q':
                x8 = x8 + 10
            elif user_input == 'K':
                x8 = x8 + 10
            elif user_input == 'A':
                x8 = x8 + 10
            elif user_input == 'Joker':
                x8 = x8 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x8 = x8 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x8_total += x8
    print(f"Puntaje de {jugador_8} en la Primera ronda: {x8}.")

    print('Segunda ronda: Una escala y un trío')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # jugador 3
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    # Jugador 4
    x4 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x4 = x4 + 10
            elif user_input == 'Q':
                x4 = x4 + 10
            elif user_input == 'K':
                x4 = x4 + 10
            elif user_input == 'A':
                x4 = x4 + 10
            elif user_input == 'Joker':
                x4 = x4 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x4 = x4 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x4_total += x4
    print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")

    # jugador 5
    x5 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_5}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x5 = x5 + 10
            elif user_input == 'Q':
                x5 = x5 + 10
            elif user_input == 'K':
                x5 = x5 + 10
            elif user_input == 'A':
                x5 = x5 + 10
            elif user_input == 'Joker':
                x5 = x5 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x5 = x5 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x5_total += x5
    print(f"Puntaje de {jugador_5} en la Primera ronda: {x5}.")

    # jugador 6
    x6 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_6}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x6 = x6 + 10
            elif user_input == 'Q':
                x6 = x6 + 10
            elif user_input == 'K':
                x6 = x6 + 10
            elif user_input == 'A':
                x6 = x6 + 10
            elif user_input == 'Joker':
                x6 = x6 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x6 = x6 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x6_total += x6
    print(f"Puntaje de {jugador_6} en la Primera ronda: {x6}.")

    # jugador 7
    x7 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_7}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x7 = x7 + 10
            elif user_input == 'Q':
                x7 = x7 + 10
            elif user_input == 'K':
                x7 = x7 + 10
            elif user_input == 'A':
                x7 = x7 + 10
            elif user_input == 'Joker':
                x7 = x7 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x7 = x7 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x7_total += x7
    print(f"Puntaje de {jugador_7} en la Primera ronda: {x7}.")

    # Jugador 8
    x8 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_8}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x8 = x8 + 10
            elif user_input == 'Q':
                x8 = x8 + 10
            elif user_input == 'K':
                x8 = x8 + 10
            elif user_input == 'A':
                x8 = x8 + 10
            elif user_input == 'Joker':
                x8 = x8 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x8 = x8 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x8_total += x8
    print(f"Puntaje de {jugador_8} en la Primera ronda: {x8}.")

    print('Trecera ronda: Dos escalas')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # jugador 3
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    # Jugador 4
    x4 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x4 = x4 + 10
            elif user_input == 'Q':
                x4 = x4 + 10
            elif user_input == 'K':
                x4 = x4 + 10
            elif user_input == 'A':
                x4 = x4 + 10
            elif user_input == 'Joker':
                x4 = x4 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x4 = x4 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x4_total += x4
    print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")

    # jugador 5
    x5 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while contador < 12:
        user_input = input(f"{jugador_5}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x5 = x5 + 10
            elif user_input == 'Q':
                x5 = x5 + 10
            elif user_input == 'K':
                x5 = x5 + 10
            elif user_input == 'A':
                x5 = x5 + 10
            elif user_input == 'Joker':
                x5 = x5 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x5 = x5 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x5_total += x5
    print(f"Puntaje de {jugador_5} en la Primera ronda: {x5}.")

    # jugador 6
    x6 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_6}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x6 = x6 + 10
            elif user_input == 'Q':
                x6 = x6 + 10
            elif user_input == 'K':
                x6 = x6 + 10
            elif user_input == 'A':
                x6 = x6 + 10
            elif user_input == 'Joker':
                x6 = x6 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x6 = x6 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x6_total += x6
    print(f"Puntaje de {jugador_6} en la Primera ronda: {x6}.")

    # jugador 7
    x7 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_7}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x7 = x7 + 10
            elif user_input == 'Q':
                x7 = x7 + 10
            elif user_input == 'K':
                x7 = x7 + 10
            elif user_input == 'A':
                x7 = x7 + 10
            elif user_input == 'Joker':
                x7 = x7 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x7 = x7 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x7_total += x7
    print(f"Puntaje de {jugador_7} en la Primera ronda: {x7}.")

    # Jugador 8
    x8 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_8}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x8 = x8 + 10
            elif user_input == 'Q':
                x8 = x8 + 10
            elif user_input == 'K':
                x8 = x8 + 10
            elif user_input == 'A':
                x8 = x8 + 10
            elif user_input == 'Joker':
                x8 = x8 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x8 = x8 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x8_total += x8
    print(f"Puntaje de {jugador_8} en la Primera ronda: {x8}.")

    print('Cuarta ronda: Tres tríos')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # jugador 3
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    # Jugador 4
    x4 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x4 = x4 + 10
            elif user_input == 'Q':
                x4 = x4 + 10
            elif user_input == 'K':
                x4 = x4 + 10
            elif user_input == 'A':
                x4 = x4 + 10
            elif user_input == 'Joker':
                x4 = x4 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x4 = x4 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x4_total += x4
    print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")

    # jugador 5
    x5 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while contador < 12:
        user_input = input(f"{jugador_5}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x5 = x5 + 10
            elif user_input == 'Q':
                x5 = x5 + 10
            elif user_input == 'K':
                x5 = x5 + 10
            elif user_input == 'A':
                x5 = x5 + 10
            elif user_input == 'Joker':
                x5 = x5 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x5 = x5 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x5_total += x5
    print(f"Puntaje de {jugador_5} en la Primera ronda: {x5}.")

    # jugador 6
    x6 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_6}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x6 = x6 + 10
            elif user_input == 'Q':
                x6 = x6 + 10
            elif user_input == 'K':
                x6 = x6 + 10
            elif user_input == 'A':
                x6 = x6 + 10
            elif user_input == 'Joker':
                x6 = x6 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x6 = x6 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x6_total += x6
    print(f"Puntaje de {jugador_6} en la Primera ronda: {x6}.")

    # jugador 7
    x7 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_7}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x7 = x7 + 10
            elif user_input == 'Q':
                x7 = x7 + 10
            elif user_input == 'K':
                x7 = x7 + 10
            elif user_input == 'A':
                x7 = x7 + 10
            elif user_input == 'Joker':
                x7 = x7 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x7 = x7 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x7_total += x7
    print(f"Puntaje de {jugador_7} en la Primera ronda: {x7}.")

    # Jugador 8
    x8 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_8}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x8 = x8 + 10
            elif user_input == 'Q':
                x8 = x8 + 10
            elif user_input == 'K':
                x8 = x8 + 10
            elif user_input == 'A':
                x8 = x8 + 10
            elif user_input == 'Joker':
                x8 = x8 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x8 = x8 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x8_total += x8
    print(f"Puntaje de {jugador_8} en la Primera ronda: {x8}.")

    print('Quinta ronda: Dos tríos y una escala')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # jugador 3
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    # Jugador 4
    x4 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x4 = x4 + 10
            elif user_input == 'Q':
                x4 = x4 + 10
            elif user_input == 'K':
                x4 = x4 + 10
            elif user_input == 'A':
                x4 = x4 + 10
            elif user_input == 'Joker':
                x4 = x4 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x4 = x4 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x4_total += x4
    print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")

    # jugador 5
    x5 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while contador < 12:
        user_input = input(f"{jugador_5}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x5 = x5 + 10
            elif user_input == 'Q':
                x5 = x5 + 10
            elif user_input == 'K':
                x5 = x5 + 10
            elif user_input == 'A':
                x5 = x5 + 10
            elif user_input == 'Joker':
                x5 = x5 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x5 = x5 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x5_total += x5
    print(f"Puntaje de {jugador_5} en la Primera ronda: {x5}.")

    # jugador 6
    x6 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_6}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x6 = x6 + 10
            elif user_input == 'Q':
                x6 = x6 + 10
            elif user_input == 'K':
                x6 = x6 + 10
            elif user_input == 'A':
                x6 = x6 + 10
            elif user_input == 'Joker':
                x6 = x6 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x6 = x6 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x6_total += x6
    print(f"Puntaje de {jugador_6} en la Primera ronda: {x6}.")

    # jugador 7
    x7 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_7}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x7 = x7 + 10
            elif user_input == 'Q':
                x7 = x7 + 10
            elif user_input == 'K':
                x7 = x7 + 10
            elif user_input == 'A':
                x7 = x7 + 10
            elif user_input == 'Joker':
                x7 = x7 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x7 = x7 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x7_total += x7
    print(f"Puntaje de {jugador_7} en la Primera ronda: {x7}.")

    # Jugador 8
    x8 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_8}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x8 = x8 + 10
            elif user_input == 'Q':
                x8 = x8 + 10
            elif user_input == 'K':
                x8 = x8 + 10
            elif user_input == 'A':
                x8 = x8 + 10
            elif user_input == 'Joker':
                x8 = x8 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x8 = x8 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x8_total += x8
    print(f"Puntaje de {jugador_8} en la Primera ronda: {x8}.")

    print('Sexta ronda: Dos escalas y un trío')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # jugador 3
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    # Jugador 4
    x4 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x4 = x4 + 10
            elif user_input == 'Q':
                x4 = x4 + 10
            elif user_input == 'K':
                x4 = x4 + 10
            elif user_input == 'A':
                x4 = x4 + 10
            elif user_input == 'Joker':
                x4 = x4 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x4 = x4 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x4_total += x4
    print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")

    # jugador 5
    x5 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while contador < 12:
        user_input = input(f"{jugador_5}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x5 = x5 + 10
            elif user_input == 'Q':
                x5 = x5 + 10
            elif user_input == 'K':
                x5 = x5 + 10
            elif user_input == 'A':
                x5 = x5 + 10
            elif user_input == 'Joker':
                x5 = x5 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x5 = x5 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x5_total += x5
    print(f"Puntaje de {jugador_5} en la Primera ronda: {x5}.")

    # jugador 6
    x6 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_6}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x6 = x6 + 10
            elif user_input == 'Q':
                x6 = x6 + 10
            elif user_input == 'K':
                x6 = x6 + 10
            elif user_input == 'A':
                x6 = x6 + 10
            elif user_input == 'Joker':
                x6 = x6 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x6 = x6 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x6_total += x6
    print(f"Puntaje de {jugador_6} en la Primera ronda: {x6}.")

    # jugador 7
    x7 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_7}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x7 = x7 + 10
            elif user_input == 'Q':
                x7 = x7 + 10
            elif user_input == 'K':
                x7 = x7 + 10
            elif user_input == 'A':
                x7 = x7 + 10
            elif user_input == 'Joker':
                x7 = x7 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x7 = x7 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x7_total += x7
    print(f"Puntaje de {jugador_7} en la Primera ronda: {x7}.")

    # Jugador 8
    x8 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_8}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x8 = x8 + 10
            elif user_input == 'Q':
                x8 = x8 + 10
            elif user_input == 'K':
                x8 = x8 + 10
            elif user_input == 'A':
                x8 = x8 + 10
            elif user_input == 'Joker':
                x8 = x8 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x8 = x8 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x8_total += x8
    print(f"Puntaje de {jugador_8} en la Primera ronda: {x8}.")

    print('Septima ronda: Tres escalas')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # jugador 3
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    # Jugador 4
    x4 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x4 = x4 + 10
            elif user_input == 'Q':
                x4 = x4 + 10
            elif user_input == 'K':
                x4 = x4 + 10
            elif user_input == 'A':
                x4 = x4 + 10
            elif user_input == 'Joker':
                x4 = x4 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x4 = x4 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x4_total += x4
    print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")

    # jugador 5
    x5 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while contador < 12:
        user_input = input(f"{jugador_5}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x5 = x5 + 10
            elif user_input == 'Q':
                x5 = x5 + 10
            elif user_input == 'K':
                x5 = x5 + 10
            elif user_input == 'A':
                x5 = x5 + 10
            elif user_input == 'Joker':
                x5 = x5 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x5 = x5 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x5_total += x5
    print(f"Puntaje de {jugador_5} en la Primera ronda: {x5}.")

    # jugador 6
    x6 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_6}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x6 = x6 + 10
            elif user_input == 'Q':
                x6 = x6 + 10
            elif user_input == 'K':
                x6 = x6 + 10
            elif user_input == 'A':
                x6 = x6 + 10
            elif user_input == 'Joker':
                x6 = x6 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x6 = x6 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x6_total += x6
    print(f"Puntaje de {jugador_6} en la Primera ronda: {x6}.")

    # jugador 7
    x7 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_7}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x7 = x7 + 10
            elif user_input == 'Q':
                x7 = x7 + 10
            elif user_input == 'K':
                x7 = x7 + 10
            elif user_input == 'A':
                x7 = x7 + 10
            elif user_input == 'Joker':
                x7 = x7 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x7 = x7 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x7_total += x7
    print(f"Puntaje de {jugador_7} en la Primera ronda: {x7}.")

    # Jugador 8
    x8 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_8}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x8 = x8 + 10
            elif user_input == 'Q':
                x8 = x8 + 10
            elif user_input == 'K':
                x8 = x8 + 10
            elif user_input == 'A':
                x8 = x8 + 10
            elif user_input == 'Joker':
                x8 = x8 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x8 = x8 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x8_total += x8
    print(f"Puntaje de {jugador_8} en la Primera ronda: {x8}.")

    print('Octava ronda: Cuatro tríos')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # jugador 3
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    # Jugador 4
    x4 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x4 = x4 + 10
            elif user_input == 'Q':
                x4 = x4 + 10
            elif user_input == 'K':
                x4 = x4 + 10
            elif user_input == 'A':
                x4 = x4 + 10
            elif user_input == 'Joker':
                x4 = x4 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x4 = x4 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x4_total += x4
    print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")

    # jugador 5
    x5 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while contador < 12:
        user_input = input(f"{jugador_5}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x5 = x5 + 10
            elif user_input == 'Q':
                x5 = x5 + 10
            elif user_input == 'K':
                x5 = x5 + 10
            elif user_input == 'A':
                x5 = x5 + 10
            elif user_input == 'Joker':
                x5 = x5 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x5 = x5 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x5_total += x5
    print(f"Puntaje de {jugador_5} en la Primera ronda: {x5}.")

    # jugador 6
    x6 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_6}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x6 = x6 + 10
            elif user_input == 'Q':
                x6 = x6 + 10
            elif user_input == 'K':
                x6 = x6 + 10
            elif user_input == 'A':
                x6 = x6 + 10
            elif user_input == 'Joker':
                x6 = x6 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x6 = x6 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x6_total += x6
    print(f"Puntaje de {jugador_6} en la Primera ronda: {x6}.")

    # jugador 7
    x7 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_7}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x7 = x7 + 10
            elif user_input == 'Q':
                x7 = x7 + 10
            elif user_input == 'K':
                x7 = x7 + 10
            elif user_input == 'A':
                x7 = x7 + 10
            elif user_input == 'Joker':
                x7 = x7 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x7 = x7 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x7_total += x7
    print(f"Puntaje de {jugador_7} en la Primera ronda: {x7}.")

    # Jugador 8
    x8 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_8}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x8 = x8 + 10
            elif user_input == 'Q':
                x8 = x8 + 10
            elif user_input == 'K':
                x8 = x8 + 10
            elif user_input == 'A':
                x8 = x8 + 10
            elif user_input == 'Joker':
                x8 = x8 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x8 = x8 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x8_total += x8
    print(f"Puntaje de {jugador_8} en la Primera ronda: {x8}.")

    print('Novena ronda: Escalera Sucia')

    # Jugador 1
    x1 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x1 = x1 + 10
            elif user_input == 'Q':
                x1 = x1 + 10
            elif user_input == 'K':
                x1 = x1 + 10
            elif user_input == 'A':
                x1 = x1 + 10
            elif user_input == 'Joker':
                x1 = x1 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x1 = x1 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x1_total += x1
    print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

    # Jugador 2
    x2 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x2 = x2 + 10
            elif user_input == 'Q':
                x2 = x2 + 10
            elif user_input == 'K':
                x2 = x2 + 10
            elif user_input == 'A':
                x2 = x2 + 10
            elif user_input == 'Joker':
                x2 = x2 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x2 = x2 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x2_total += x2
    print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

    # jugador 3
    x3 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x3 = x3 + 10
            elif user_input == 'Q':
                x3 = x3 + 10
            elif user_input == 'K':
                x3 = x3 + 10
            elif user_input == 'A':
                x3 = x3 + 10
            elif user_input == 'Joker':
                x3 = x3 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x3 = x3 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x3_total += x3
    print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

    # Jugador 4
    x4 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    user_input = ''
    while user_input != contador < 12:
        user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x4 = x4 + 10
            elif user_input == 'Q':
                x4 = x4 + 10
            elif user_input == 'K':
                x4 = x4 + 10
            elif user_input == 'A':
                x4 = x4 + 10
            elif user_input == 'Joker':
                x4 = x4 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x4 = x4 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x4_total += x4
    print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")

    # jugador 5
    x5 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while contador < 12:
        user_input = input(f"{jugador_5}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x5 = x5 + 10
            elif user_input == 'Q':
                x5 = x5 + 10
            elif user_input == 'K':
                x5 = x5 + 10
            elif user_input == 'A':
                x5 = x5 + 10
            elif user_input == 'Joker':
                x5 = x5 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x5 = x5 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x5_total += x5
    print(f"Puntaje de {jugador_5} en la Primera ronda: {x5}.")

    # jugador 6
    x6 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_6}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x6 = x6 + 10
            elif user_input == 'Q':
                x6 = x6 + 10
            elif user_input == 'K':
                x6 = x6 + 10
            elif user_input == 'A':
                x6 = x6 + 10
            elif user_input == 'Joker':
                x6 = x6 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x6 = x6 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x6_total += x6
    print(f"Puntaje de {jugador_6} en la Primera ronda: {x6}.")

    # jugador 7
    x7 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_7}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x7 = x7 + 10
            elif user_input == 'Q':
                x7 = x7 + 10
            elif user_input == 'K':
                x7 = x7 + 10
            elif user_input == 'A':
                x7 = x7 + 10
            elif user_input == 'Joker':
                x7 = x7 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x7 = x7 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x7_total += x7
    print(f"Puntaje de {jugador_7} en la Primera ronda: {x7}.")

    # Jugador 8
    x8 = 0
    contador = 0
    cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
    while user_input != contador < 12:
        user_input = input(f"{jugador_8}, ingrese las cartas que tienes: ")
        if user_input in cartas_permitidas:
            if user_input == 'J':
                x8 = x8 + 10
            elif user_input == 'Q':
                x8 = x8 + 10
            elif user_input == 'K':
                x8 = x8 + 10
            elif user_input == 'A':
                x8 = x8 + 10
            elif user_input == 'Joker':
                x8 = x8 + 30
            elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                x8 = x8 + int(user_input)
            contador += 1
        else:
            print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
    x8_total += x8
    print(f"Puntaje de {jugador_8} en la Primera ronda: {x8}.")

    N = input('Quieren hacer la Escala Real (SI o NO): ')
    if N == 'SI':
        print('Decima ronda: Escalera Real')
        # Jugador 1
        x1 = 0
        contador = 0
        cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
        user_input = ''
        while user_input != contador < 12:
            user_input = input(f"{jugador_1}, ingrese las cartas que tienes: ")
            if user_input in cartas_permitidas:
                if user_input == 'J':
                    x1 = x1 + 10
                elif user_input == 'Q':
                    x1 = x1 + 10
                elif user_input == 'K':
                    x1 = x1 + 10
                elif user_input == 'A':
                    x1 = x1 + 10
                elif user_input == 'Joker':
                    x1 = x1 + 30
                elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                    x1 = x1 + int(user_input)
                contador += 1
            else:
                print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
        x1_total += x1
        print(f"Puntaje de {jugador_1} en la Primera ronda: {x1}.")

        # Jugador 2
        x2 = 0
        contador = 0
        cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
        user_input = ''
        while user_input != contador < 12:
            user_input = input(f"{jugador_2}, ingrese las cartas que tienes: ")
            if user_input in cartas_permitidas:
                if user_input == 'J':
                    x2 = x2 + 10
                elif user_input == 'Q':
                    x2 = x2 + 10
                elif user_input == 'K':
                    x2 = x2 + 10
                elif user_input == 'A':
                    x2 = x2 + 10
                elif user_input == 'Joker':
                    x2 = x2 + 30
                elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                    x2 = x2 + int(user_input)
                contador += 1
            else:
                print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
        x2_total += x2
        print(f"Puntaje de {jugador_2} en la Primera ronda: {x2}.")

        # jugador 3
        x3 = 0
        contador = 0
        cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
        user_input = ''
        while user_input != contador < 12:
            user_input = input(f"{jugador_3}, ingrese las cartas que tienes: ")
            if user_input in cartas_permitidas:
                if user_input == 'J':
                    x3 = x3 + 10
                elif user_input == 'Q':
                    x3 = x3 + 10
                elif user_input == 'K':
                    x3 = x3 + 10
                elif user_input == 'A':
                    x3 = x3 + 10
                elif user_input == 'Joker':
                    x3 = x3 + 30
                elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                    x3 = x3 + int(user_input)
                contador += 1
            else:
                print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
        x3_total += x3
        print(f"Puntaje de {jugador_3} en la Primera ronda: {x2}.")

        # Jugador 4
        x4 = 0
        contador = 0
        cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
        user_input = ''
        while user_input != contador < 12:
            user_input = input(f"{jugador_4}, ingrese las cartas que tienes: ")
            if user_input in cartas_permitidas:
                if user_input == 'J':
                    x4 = x4 + 10
                elif user_input == 'Q':
                    x4 = x4 + 10
                elif user_input == 'K':
                    x4 = x4 + 10
                elif user_input == 'A':
                    x4 = x4 + 10
                elif user_input == 'Joker':
                    x4 = x4 + 30
                elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                    x4 = x4 + int(user_input)
                contador += 1
            else:
                print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
        x4_total += x4
        print(f"Puntaje de {jugador_4} en la Primera ronda: {x4}.")

        # jugador 5
        x5 = 0
        contador = 0
        cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
        while contador < 12:
            user_input = input(f"{jugador_5}, ingrese las cartas que tienes: ")
            if user_input in cartas_permitidas:
                if user_input == 'J':
                    x5 = x5 + 10
                elif user_input == 'Q':
                    x5 = x5 + 10
                elif user_input == 'K':
                    x5 = x5 + 10
                elif user_input == 'A':
                    x5 = x5 + 10
                elif user_input == 'Joker':
                    x5 = x5 + 30
                elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                    x5 = x5 + int(user_input)
                contador += 1
            else:
                print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
        x5_total += x5
        print(f"Puntaje de {jugador_5} en la Primera ronda: {x5}.")

        # jugador 6
        x6 = 0
        contador = 0
        cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
        while user_input != contador < 12:
            user_input = input(f"{jugador_6}, ingrese las cartas que tienes: ")
            if user_input in cartas_permitidas:
                if user_input == 'J':
                    x6 = x6 + 10
                elif user_input == 'Q':
                    x6 = x6 + 10
                elif user_input == 'K':
                    x6 = x6 + 10
                elif user_input == 'A':
                    x6 = x6 + 10
                elif user_input == 'Joker':
                    x6 = x6 + 30
                elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                    x6 = x6 + int(user_input)
                contador += 1
            else:
                print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
        x6_total += x6
        print(f"Puntaje de {jugador_6} en la Primera ronda: {x6}.")

        # jugador 7
        x7 = 0
        contador = 0
        cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
        while user_input != contador < 12:
            user_input = input(f"{jugador_7}, ingrese las cartas que tienes: ")
            if user_input in cartas_permitidas:
                if user_input == 'J':
                    x7 = x7 + 10
                elif user_input == 'Q':
                    x7 = x7 + 10
                elif user_input == 'K':
                    x7 = x7 + 10
                elif user_input == 'A':
                    x7 = x7 + 10
                elif user_input == 'Joker':
                    x7 = x7 + 30
                elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                    x7 = x7 + int(user_input)
                contador += 1
            else:
                print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
        x7_total += x7
        print(f"Puntaje de {jugador_7} en la Primera ronda: {x7}.")

        # Jugador 8
        x8 = 0
        contador = 0
        cartas_permitidas = ['J', 'Q', 'K', 'A', 'Joker'] + [str(i) for i in range(2, 11)]
        while user_input != contador < 12:
            user_input = input(f"{jugador_8}, ingrese las cartas que tienes: ")
            if user_input in cartas_permitidas:
                if user_input == 'J':
                    x8 = x8 + 10
                elif user_input == 'Q':
                    x8 = x8 + 10
                elif user_input == 'K':
                    x8 = x8 + 10
                elif user_input == 'A':
                    x8 = x8 + 10
                elif user_input == 'Joker':
                    x8 = x8 + 30
                elif user_input.isdigit() and 2 <= int(user_input) <= 10:
                    x8 = x8 + int(user_input)
                contador += 1
            else:
                print("Entrada no válida. Por favor, ingrese una carta válida o un número entre 2 y 10.")
        x8_total += x8
        print(f"Puntaje de {jugador_8} en la Primera ronda: {x8}.")


    else:
        print('Resultados')
        print(f"Puntaje de {jugador_1} es {x1_total}")
        print(f"Puntaje de {jugador_2} es {x2_total}")
        print(f"Puntaje de {jugador_3} es {x3_total}")
        print(f"Puntaje de {jugador_4} es {x4_total}")
        print(f"Puntaje de {jugador_5} es {x5_total}")
        print(f"Puntaje de {jugador_6} es {x6_total}")
        print(f"Puntaje de {jugador_7} es {x7_total}")
        print(f"Puntaje de {jugador_8} es {x8_total}")


elif jugadoes >= 8:
    print('el numeor maximo de juagadores son 8')

else:
    jugadoes <= 1
    print('no puedes jugar solo')