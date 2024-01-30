class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre # Atributo protegido
        self._edad = edad # Atributo protegido

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_edad(self):
        return self._edad

    def set_edad(self, edad):
        self._edad = edad
# Uso de la clase
persona = Persona("Jorge", 36)
print(persona.get_nombre())  # Output: Jorge
persona.set_nombre("Carlos")
print(persona.get_nombre())  # Output: Carlos

#(En este caso, los atributos _nombre y _edad se encuentran encapsulados y se accede a ellos mediante métodos get y set,
#lo que permite un control más estricto sobre su modificación y acceso.)

