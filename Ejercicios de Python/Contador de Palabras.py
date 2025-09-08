class ContadorPalabras:
    def __init__(self):
        self.contador = 0

    def contar(self, texto):
        palabras = texto.split()
        cantidad = len(palabras)
        self.contador += cantidad
        print(f"Se encontraron {cantidad} palabras en el texto.")

    def obtener_contador(self):
        return self.contador  # Devuelve el valor actual del contador

# Crear una instancia de la clase
mi_contador = ContadorPalabras()

# Usar el método contar con una cadena de texto
texto_usuario = input("Ingresa una frase para contar sus palabras: ")
mi_contador.contar(texto_usuario)

# Mostrar el resultado final
print("Cantidad total de palabras contadas:", mi_contador.obtener_contador())