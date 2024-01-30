#Program de Registro de helados de tres sabores
# Este programa tiene dos clases: Helado que representa un helado individual y RegistroHelados que gestiona una lista de helados. Los constructores inicializan los atributos, y los destructores simplemente imprimen mensajes.
# Los comentarios explican el funcionamiento de los métodos y en qué situaciones se activan los constructores y destructores.
class Helado:
    def __init__(self, sabor, topping):
        """
        Constructor de la clase Helado.

        :param sabor: Sabor principal del helado.
        :param topping: Topping del helado.
        """
        self.sabor = sabor
        self.topping = topping
        print(f"Se ha creado un nuevo helado de {self.sabor} con topping de {self.topping}.")

    def __del__(self):
        """
        Destructor de la clase Helado.
        Realiza alguna forma de limpieza o cierre de recursos (si es aplicable).
        En este ejemplo, simplemente imprime un mensaje al destruir el objeto.
        """
        print(f"El helado de {self.sabor} con topping de {self.topping} ha sido eliminado del registro.")

class RegistroHelados:
    def __init__(self):
        """
        Constructor de la clase RegistroHelados.
        Inicializa la lista de helados al crear una nueva instancia.
        """
        self.lista_helados = []
        print("Registro de helados creado.")

    def agregar_helado(self, helado):
        """
        Agrega un helado a la lista de helados.

        :param helado: Instancia de la clase Helado.
        """
        self.lista_helados.append(helado)
        print(f"Helado de {helado.sabor} con topping de {helado.topping} añadido al registro.")

    def mostrar_helados(self):
        """
        Muestra la lista de helados en el registro.
        """
        print("Lista de helados:")
        for helado in self.lista_helados:
            print(f"Sabor: {helado.sabor} - Topping: {helado.topping}")

    def __del__(self):
        """
        Destructor de la clase RegistroHelados.
        Realiza alguna limpieza al cerrar el programa, si es aplicable.
        En este ejemplo, simplemente imprime un mensaje al destruir el objeto.
        """
        print("Cerrando el registro de helados. Limpieza final.")

# Crear instancias de la clase Helado
helado1 = Helado("Chocolate", "Nueces")
helado2 = Helado("Vainilla", "Caramelo")
helado3 = Helado("Fresa", "Chispas de chocolate")

# Crear instancia de la clase RegistroHelados
registro_helados = RegistroHelados()

# Agregar helados al registro
registro_helados.agregar_helado(helado1)
registro_helados.agregar_helado(helado2)
registro_helados.agregar_helado(helado3)

# Mostrar la lista de helados en el registro
registro_helados.mostrar_helados()

# Al finalizar el programa, las instancias y el registro serán eliminados automáticamente, activando sus destructores.
