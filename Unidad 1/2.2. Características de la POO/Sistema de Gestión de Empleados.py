#Programa: Sistema de Gestión de Empleados
#Este programa simula un sistema de gestión de empleados.
#Utiliza una clase Empleado para representar a los empleados de una empresa,
#Utiliza una clase Departamento para manejar la asignación de empleados a departamentos. El departamento tiene métodos para agregar empleados, mostrar la lista de empleados y calcular el salario total del departamento.
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

class Departamento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def mostrar_empleados(self):
        print(f"Empleados en el departamento {self.nombre}:")
        for empleado in self.empleados:
            print(f"- {empleado.nombre}")

    def calcular_salario_total(self):
        total = 0
        for empleado in self.empleados:
            total += empleado.salario
        return total

empleado1 = Empleado("Mauricio Ponce", 2000)
empleado2 = Empleado("Elizabeth Castillo", 2500)

departamento = Departamento("Ventas")
departamento.agregar_empleado(empleado1)
departamento.agregar_empleado(empleado2)

departamento.mostrar_empleados()
print(f"Salario total del departamento de ventas: ${departamento.calcular_salario_total()}")
