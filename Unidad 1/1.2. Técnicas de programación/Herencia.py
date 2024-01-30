class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        print("El vehículo está acelerando")

class Coche(Vehiculo):
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo)
        self.color = color

    def abrir_puertas(self):
        print("Las puertas del coche están abiertas")

coche = Coche("Chevrolet", "Camaro", "Azul")
print(coche.marca)  # Output: Chevrolet
coche.acelerar()  # Output: El vehículo está acelerando
coche.abrir_puertas()  # Output: Las puertas del coche están abiertas

#( En el ejemplo, la clase Coche hereda de la clase Vehiculo, lo que le permite adquirir los atributos y métodos de la clase padre,
# y además define su propio método abrir_puertas.)

