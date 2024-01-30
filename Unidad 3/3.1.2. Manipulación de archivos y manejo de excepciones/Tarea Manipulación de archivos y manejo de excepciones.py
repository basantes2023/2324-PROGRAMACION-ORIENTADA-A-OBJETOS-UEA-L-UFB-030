#Este programa implementa las clases Producto e Inventario que representan los productos y el inventario, respectivamente. Los productos tienen atributos como el ID, nombre, cantidad y precio, y la clase Inventario contiene una lista de productos y métodos para agregar, eliminar, actualizar, buscar y mostrar productos.
#La información del inventario se almacena en un archivo llamado "inventario.txt" utilizando el módulo pickle. Al iniciar el programa, los productos existentes se cargan automáticamente desde el archivo para reconstruir el inventario.
#Se implementa el manejo de excepciones para capturar errores relacionados con la manipulación de archivos, como FileNotFoundError y PermissionError.
#La información del inventario se almacena en un archivo llamado "inventario.txt" utilizando el módulo pickle. Al iniciar el programa, los productos existentes se cargan automáticamente desde el archivo para reconstruir el inventario.


import pickle


class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters y setters para cada atributo
    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                raise ValueError("El ID del producto ya existe en el inventario.")
        self.productos.append(producto)
        self.guardar_inventario()

    def eliminar_producto(self, id):
        for producto in self.productos:
            if producto.get_id() == id:
                self.productos.remove(producto)
                self.guardar_inventario()
                return
        raise ValueError("No se encontró ningún producto con el ID especificado.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.get_id() == id:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                self.guardar_inventario()
                return
        raise ValueError("No se encontró ningún producto con el ID especificado.")

    def buscar_productos(self, nombre):
        resultado = []
        for producto in self.productos:
            if nombre.lower() in producto.get_nombre().lower():
                resultado.append(producto)
        return resultado

    def mostrar_inventario(self):
        for producto in self.productos:
            print("ID: {}, Nombre: {}, Cantidad: {}, Precio: {}".format(
                producto.get_id(), producto.get_nombre(), producto.get_cantidad(), producto.get_precio()))

    def guardar_inventario(self):
        with open("inventario.txt", "wb") as archivo:
            pickle.dump(self.productos, archivo)

    def cargar_inventario(self):
        try:
            with open("inventario.txt", "rb") as archivo:
                self.productos = pickle.load(archivo)
        except FileNotFoundError:
            # Si el archivo no existe, se crea uno vacío
            self.guardar_inventario()
        except PermissionError:
            print("No se tienen permisos de escritura para el archivo de inventario.")


def mostrar_menu():
    print("=== Sistema de Gestión de Inventarios ===")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar productos")
    print("5. Mostrar inventario")
    print("0. Salir")


def agregar_producto(inventario):
    id = input("Ingrese el ID del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad del producto: "))
    precio = float(input("Ingrese el precio del producto: "))

    producto = Producto(id, nombre, cantidad, precio)
    try:
        inventario.agregar_producto(producto)
        print("Producto agregado exitosamente.")
    except ValueError as e:
        print(str(e))


def eliminar_producto(inventario):
    id = input("Ingrese el ID del producto a eliminar: ")
    try:
        inventario.eliminar_producto(id)
        print("Producto eliminado exitosamente.")
    except ValueError as e:
        print(str(e))


def actualizar_producto(inventario):
    id = input("Ingrese el ID del producto a actualizar: ")
    cantidad = input("Ingrese la nueva cantidad del producto (dejar en blanco para no actualizar): ")
    precio = input("Ingrese el nuevo precio del producto (dejar en blanco para no actualizar): ")

    try:
        cantidad = int(cantidad) if cantidad != "" else None
        precio = float(precio) if precio != "" else None
        inventario.actualizar_producto(id, cantidad, precio)
        print("Producto actualizado exitosamente.")
    except ValueError as e:
        print(str(e))


def buscar_productos(inventario):
    nombre = input("Ingrese el nombre del producto a buscar: ")
    resultados = inventario.buscar_productos(nombre)
    if len(resultados) > 0:
        print("Resultados de búsqueda:")
        for producto in resultados:
            print("ID: {}, Nombre: {}, Cantidad: {}, Precio: {}".format(
                producto.get_id(), producto.get_nombre(), producto.get_cantidad(), producto.get_precio()))
    else:
        print("No se encontraron productos con el nombre especificado.")


def mostrar_inventario(inventario):
    inventario.mostrar_inventario()


def main():
    inventario = Inventario()
    inventario.cargar_inventario()

    while True:
        mostrar_menu()
        opcion = input("Ingrese la opción deseada: ")
        print()

        if opcion == "1":
            agregar_producto(inventario)
        elif opcion == "2":
            eliminar_producto(inventario)
        elif opcion == "3":
            actualizar_producto(inventario)
        elif opcion == "4":
            buscar_productos(inventario)
        elif opcion == "5":
            mostrar_inventario(inventario)
        elif opcion == "0":
            inventario.guardar_inventario()
            print("¡Gracias por usar el Sistema de Gestión de Inventarios!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


if __name__ == "__main__":
    main()