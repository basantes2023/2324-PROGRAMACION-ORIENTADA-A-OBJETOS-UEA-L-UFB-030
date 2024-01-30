class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau guau")

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau miau")

perro = Perro("Fido", 3)
gato = Gato("Garfield", 5)

perro.hacer_sonido()  # Output: Guau guau
gato.hacer_sonido()  # Output: Miau miau

#(Las clases Perro y Gato heredan de la clase Animal y proporcionan su propia implementación del método hacer_sonido,
# mostrando así la abstracción al permitir que cada objeto realice su propio sonido sin necesidad de conocer los detalles internos.)