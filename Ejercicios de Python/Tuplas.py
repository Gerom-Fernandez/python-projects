palabras = ("manzana", "banana", "cereza")

palabra_buscar = input("Ingresa una palabra para buscar en la tupla: ")

if palabra_buscar in palabras:
    print(f"La palabra '{palabra_buscar}' está en la tupla.")
else:
    print(f"La palabra '{palabra_buscar}' no está en la tupla.")