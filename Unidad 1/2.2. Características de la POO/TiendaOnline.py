# Programa: Tienda Online  Agregar al carrito producto y paga
# Este programa simula una tienda online. Utiliza una clase Producto para representar los productos en venta, y una clase Carrito para manejar las compras de los clientes.
# El carrito tiene métodos para agregar productos, calcular el total de la compra y realizar el pago.

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_informacion(self):
        print("Nombre:", self.nombre)
        print("Precio:", self.precio)
        print("Stock:", self.stock)

class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_carrito(self):
        for producto in self.productos:
            producto.mostrar_informacion()

    def calcular_total(self):
        total = 0
        for producto in self.productos:
            total += producto.precio
        return total

# Ejemplo de uso
producto1 = Producto("Laptop hp", 1000, 5)
producto2 = Producto("Teléfono Xiaomi", 500, 10)

carrito = Carrito()
carrito.agregar_producto(producto1)
carrito.agregar_producto(producto2)

carrito.mostrar_carrito()

total = carrito.calcular_total()
print("Total a pagar:", total)
