# Definición de la clase Persona
class Persona:
    def __init__(self, nombre, edad):
        # Constructor que inicializa los atributos nombre y edad
        self.nombre = nombre
        self.edad = edad

    # Método que imprime un saludo con el nombre y edad de la persona
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Crear la primera instancia de la clase Persona
persona1 = Persona("Juan", 30)

# Llamar al método saludar de la primera persona
persona1.saludar()

# Crear la segunda instancia de la clase Persona
persona2 = Persona("María", 25)

# Llamar al método saludar de la segunda persona
persona2.saludar()
