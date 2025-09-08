# Este es un proyecto muy simple para sumar el valor de las cartas de carioca
# Reglas: J,Q,K,A = 10 puntos; JOKER = 30; 2-10 = su valor numérico

def valor_carta(inp):
    """Devuelve (nombre_normalizado, puntos) o (None, None) si inválida."""
    if inp in {"J", "Q", "K", "A"}:
        return inp, 10
    if inp == "JOKER":
        return inp, 30
    # si es número entre 2 y 10
    if inp.isdigit():
        v = int(inp)
        if 2 <= v <= 10:
            return str(v), v
    return None, None

print("PROYECTO: sumar el valor de las cartas de carioca")
print("Puedes indicar cuántas cartas vas a ingresar o dejar en blanco para usar modo libre (termina con 'FIN').")

# Preguntar cantidad (opcional)
n_input = input("¿Cuántas cartas tienes? (ej: 5) — o presiona Enter para modo libre: ").strip()
max_cartas = None
if n_input.isdigit():
    max_cartas = int(n_input)
    if max_cartas <= 0:
        max_cartas = None  # si el usuario pone 0 o negativo, pasamos a modo libre

total = 0
contador = 0
cartas = []  # lista de tuplas (nombre, puntos)

while True:
    # parar si llegamos al máximo (si el usuario había indicado un número)
    if max_cartas is not None and contador >= max_cartas:
        print("\nHas llegado al número de cartas indicado.")
        break

    entrada = input(f"Ingrese carta #{contador+1} (J,Q,K,A,JOKER o 2-10). Escribe 'FIN' para terminar: ").strip().upper()

    # permitir terminar en cualquier momento
    if entrada == "" or entrada == "FIN":
        print("Finalizando ingreso de cartas...")
        break

    nombre_norm, puntos = valor_carta(entrada)
    if nombre_norm is None:
        print("Entrada no válida. Ingresa J, Q, K, A, JOKER o un número entre 2 y 10.")
        continue  # no contamos esta entrada, pedimos otra

    # agregar al conteo y al total
    cartas.append((nombre_norm, puntos))
    contador += 1
    total += puntos

    print(f"-> Agregaste: {nombre_norm} ({puntos} pts). Cartas ingresadas: {contador}. Puntaje parcial: {total}.")

# Resumen final
print("\n===== RESUMEN =====")
if cartas:
    for i, (n, p) in enumerate(cartas, start=1):
        print(f"{i}. {n} -> {p} pts")
else:
    print("No ingresaste cartas.")
print(f"Puntaje TOTAL: {total} pts")
