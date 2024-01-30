#Este programa utiliza una clase Producto para representar cada producto en el inventario,y una clase Inventario que contiene una lista de productos y proporciona métodos para agregar, eliminar, actualizar y buscar productos.
#Los productos se guardan en una base de datos, utilizando las funciones crear_tabla, guardar_producto y cargar_productos para crear la tabla en la base de datos, guardar un producto en la base de datos y cargar los productos desde la base de datos, respectivamente.
#La interfaz de usuario se implementa en un bucle while que muestra un menú interactivo en la consola y solicita al usuario que ingrese una opción. Dependiendo de la opción seleccionada, se llaman a los métodos correspondientes de la clase Inventario.

import sqlite3

# Clase Producto
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters y setters
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

# Clase Inventario
class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, id):
        for producto in self.productos:
            if producto.get_id() == id:
                self.productos.remove(producto)
                break

    def actualizar_cantidad(self, id, cantidad):
        for producto in self.productos:
            if producto.get_id() == id:
                producto.set_cantidad(cantidad)
                break

    def actualizar_precio(self, id, precio):
        for producto in self.productos:
            if producto.get_id() == id:
                producto.set_precio(precio)
                break

    def buscar_producto(self, nombre):
        resultados = []
        for producto in self.productos:
            if nombre.lower() in producto.get_nombre().lower():
                resultados.append(producto)
        return resultados

    def mostrar_productos(self):
        for producto in self.productos:
            print(f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: {producto.get_precio()}")

# Funciones de base de datos
def crear_tabla():
    conn = sqlite3.connect("inventario.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS productos
                 (id INTEGER PRIMARY KEY, nombre TEXT, cantidad INTEGER, precio REAL)''')
    conn.commit()
    conn.close()

def guardar_producto(producto):
    conn = sqlite3.connect("inventario.db")
    c = conn.cursor()
    c.execute("INSERT INTO productos VALUES (?, ?, ?, ?)", (producto.get_id(), producto.get_nombre(), producto.get_cantidad(), producto.get_precio()))
    conn.commit()
    conn.close()

def cargar_productos():
    conn = sqlite3.connect("inventario.db")
    c = conn.cursor()
    c.execute("SELECT * FROM productos")
    filas = c.fetchall()
    inventario = Inventario()
    for fila in filas:
        producto = Producto(fila[0], fila[1], fila[2], fila[3])
        inventario.agregar_producto(producto)
    conn.close()
    return inventario

# Crear tabla en la base de datos
crear_tabla()

# Cargar productos desde la base de datos
inventario = cargar_productos()

# Interfaz de usuario en la consola
while True:
    print("=== Sistema de Gestión de Inventarios ===")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar cantidad de producto")
    print("4. Actualizar precio de producto")
    print("5. Buscar producto por nombre")
    print("6. Mostrar todos los productos")
    print("7. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        print("=== Agregar producto ===")
        id = input("Ingrese el ID del producto: ")
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad del producto: "))
        precio = float(input("Ingrese el precio del producto: "))
        producto = Producto(id, nombre, cantidad, precio)
        inventario.agregar_producto(producto)
        guardar_producto(producto)
        print("Producto agregado correctamente.")

    elif opcion == "2":
        print("=== Eliminar producto ===")
        id = input("Ingrese el ID del producto a eliminar: ")
        inventario.eliminar_producto(id)
        print("Producto eliminado correctamente.")

    elif opcion == "3":
        print("=== Actualizar cantidad de producto ===")
        id = input("Ingrese el ID del producto a actualizar: ")
        cantidad = int(input("Ingrese la nueva cantidad del producto: "))
        inventario.actualizar_cantidad(id, cantidad)
        print("Cantidad de producto actualizada correctamente.")

    elif opcion == "4":
        print("=== Actualizar precio de producto ===")
        id = input("Ingrese el ID del producto a actualizar: ")
        precio = float(input("Ingrese el nuevo precio del producto: "))
        inventario.actualizar_precio(id, precio)
        print("Precio de producto actualizado correctamente.")

    elif opcion == "5":
        print("=== Buscar producto por nombre ===")
        nombre = input("Ingrese el nombre del producto a buscar: ")
        resultados = inventario.buscar_producto(nombre)
        if len(resultados) == 0:
            print("No se encontraron productos con ese nombre.")
        else:
            print("Resultados de la búsqueda:")
            for producto in resultados:
                print(f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: {producto.get_precio()}")

    elif opcion == "6":
        print("=== Mostrar todos los productos ===")
        inventario.mostrar_productos()

    elif opcion == "7":
        print("Gracias por utilizar el sistema de gestión de inventarios. ¡Hasta luego!")
        break

    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")