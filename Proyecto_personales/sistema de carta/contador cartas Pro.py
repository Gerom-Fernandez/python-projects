'''
El juego de cartas Carioca se puede jugar con un máximo de 6 jugadores1. 
Sin embargo, el juego es idealmente para 4 jugadores. 
Mientras más jugadores participen, la dificultad de armar el juego deseado crece

Dos tríos
Una escala y un trío
Dos escalas
Tres tríos
Dos tríos y una escala
Dos escalas y un trío
Tres escalas
Cuatro tríos
Escalera Sucia (13 cartas): Una escala del As al Rey sin importar el color o la pinta.
Escalera Real (13 cartas): Una escala del As al Rey de la misma pinta

'''
2# Diccionario de rondas: nombre -> número de cartas que requiere
RONDAS = [
    ("Dos tríos", 12),
    ("Una escala y un trío", 12),
    ("Dos escalas", 12),
    ("Tres tríos", 12),
    ("Dos tríos y una escala", 12),
    ("Dos escalas y un trío", 12),
    ("Tres escalas", 12),
    ("Cuatro tríos", 12),
    ("Escalera Sucia", 13),
    ("Escalera Real", 13),
]

# Puntos de las cartas
def valor_carta(carta: str) -> int | None:
    carta = carta.upper()
    if carta in ["J", "Q", "K", "A"]:
        return 10
    if carta == "JOKER":
        return 30
    if carta.isdigit() and 2 <= int(carta) <= 10:
        return int(carta)
    return None

def ingresar_cartas(jugador, num_cartas):
    """Pide las cartas de un jugador hasta completar num_cartas"""
    total = 0
    cartas = []
    while len(cartas) < num_cartas:
        entrada = input(f"{jugador}, ingresa carta {len(cartas)+1}/{num_cartas} (o 'FIN' para terminar): ").strip().upper()
        if entrada == "FIN":
            break
        puntos = valor_carta(entrada)
        if puntos is None:
            print("Carta inválida. Intenta con J, Q, K, A, Joker o 2-10.")
            continue
        cartas.append(entrada)
        total += puntos
        print(f"✔ {entrada} vale {puntos} puntos. Parcial: {total}")
    return total

# Inicio del juego
jugadores = int(input("¿Cuántos jugadores van a participar? (máx. 6): "))
if jugadores < 2 or jugadores > 6:
    print("El número de jugadores debe estar entre 2 y 6.")
    exit()

nombres = [input(f"Nombre del jugador {i+1}: ") for i in range(jugadores)]
puntuaciones = {nombre: 0 for nombre in nombres}

# Rondas
for ronda, num_cartas in RONDAS:
    print(f"\n=== Ronda: {ronda} ({num_cartas} cartas) ===")
    for nombre in nombres:
        puntos = ingresar_cartas(nombre, num_cartas)
        puntuaciones[nombre] += puntos
        print(f"Puntaje de {nombre} en esta ronda: {puntos}")
    print("\nMarcador parcial:")
    for nombre, puntaje in puntuaciones.items():
        print(f"   {nombre}: {puntaje}")

print("\n=== RESULTADOS FINALES ===")
for nombre, puntaje in puntuaciones.items():
    print(f"{nombre}: {puntaje} puntos")