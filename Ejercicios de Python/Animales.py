from abc import ABC, abstractmethod

# Superclase abstracta
class Animal(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def hablar(self):
        pass

# Subclase Perro
class Perro(Animal):
    def hablar(self):
        return "Guau"

# Subclase Gato
class Gato(Animal):
    def hablar(self):
        return "Miau"

# Crear instancias
mi_perro = Perro("Firulais")
mi_gato = Gato("Mishito")

# Mostrar resultados
print(f"{mi_perro.nombre} dice: {mi_perro.hablar()}")
print(f"{mi_gato.nombre} dice: {mi_gato.hablar()}")