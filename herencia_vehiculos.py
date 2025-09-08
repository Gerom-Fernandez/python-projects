class vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def arrancar(self):
        print(f"{self.marca} {self.modelo} esta arrancando")

class coche(vehiculo):
    def acelerar(self):
        print(f"{self.marca} {self.modelo} esta haciendo un caballito")

class motocicleta(vehiculo):
    def arrancar(self):
        print(f"{self.marca} {self.modelo} esta haciendo un caballito")

coche = coche("Toyota", "Camry")
motocicleta = motocicleta("Harley-Davidson", "Sportster")

print(f"Coche marca y modelo: {coche.marca}, {coche.modelo}")
print(f"Motocicleta marca y modelo: {motocicleta.marca}, {motocicleta.modelo}")

print(coche.acelerar())
print(motocicleta.arrancar())