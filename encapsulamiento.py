# Ejemplo de Encapsulamiento en Programación Orientada a Objetos (POO)
class encap:
    def __init__(self):
        # Atributo privado (no debería modificarse desde fuera de la clase)
        self.__numero = 0

    # Método que usa el atributo privado
    def operacion(self):
        print(self.__numero + 20)

    # Método que retorna el valor actual del atributo privado
    def resultado(self):
        return self.__numero

# Crear objeto de la clase
ejemplo = encap()

# Llamar al método operacion (suma el atributo privado con 20)
ejemplo.operacion()

# Intento de modificar el atributo privado desde fuera (NO surte efecto real)
ejemplo.__numero = 100

# Mostrar el valor real del atributo privado (se mantiene en 0)
print(ejemplo.resultado())
