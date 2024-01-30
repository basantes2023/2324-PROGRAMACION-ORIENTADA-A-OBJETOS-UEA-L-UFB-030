
# Programa de Gestion Empleados
#Este programa cumple con lo solicitado:
#Herencia: La clase Desarrollador y la clase Gerente heredan de la clase base Empleado.
#Encapsulación: Se utiliza la doble barra baja (__) para encapsular los atributos nombre, edad y salario.
#Polimorfismo: El método calcular_bono es sobrescrito en las clases derivadas Desarrollador y Gerente.
class Empleado:
    def __init__(self, nombre, edad, salario):
        self.__nombre = nombre     #Encapsula el atributo nombre
        self.__edad = edad         #Encapsula el atributo edad
        self.__salario = salario   #Encapsula el atributo salario

    def obtener_nombre(self):
        return self.__nombre

    def obtener_edad(self):
        return self.__edad

    def obtener_salario(self):
        return self.__salario

    def calcular_bono(self):
        return 0  # Método que será sobrescrito por las clases derivadas

class Desarrollador(Empleado):
    def __init__(self, nombre, edad, salario, lenguaje):
        super().__init__(nombre, edad, salario)
        self.__lenguaje = lenguaje

    def obtener_lenguaje(self):
        return self.__lenguaje

    def calcular_bono(self):
        return self.obtener_salario() * 0.1  # Bono del 10% para desarrolladores

class Gerente(Empleado):
    def __init__(self, nombre, edad, salario, nivel):
        super().__init__(nombre, edad, salario)
        self.__nivel = nivel

    def obtener_nivel(self):
        return self.__nivel

    def calcular_bono(self):
        return self.obtener_salario() * 0.15  # Bono del 15% para gerentes

# Creación de instancias y demostración
desarrollador1 = Desarrollador("Carlos", 28, 60000, "Python")
gerente1 = Gerente("Laura", 35, 80000, "Senior")

print(f"{desarrollador1.obtener_nombre()} es un desarrollador de {desarrollador1.obtener_edad()} años, gana ${desarrollador1.obtener_salario()} y trabaja con {desarrollador1.obtener_lenguaje()}.")
print(f"{gerente1.obtener_nombre()} es un gerente de {gerente1.obtener_edad()} años, gana ${gerente1.obtener_salario()} y tiene el nivel {gerente1.obtener_nivel()}.")

# Uso de polimorfismo al llamar al método calcular_bono
empleados = [desarrollador1, gerente1]
for empleado in empleados:
    print(f"{empleado.obtener_nombre()} recibe un bono de ${empleado.calcular_bono()}")
