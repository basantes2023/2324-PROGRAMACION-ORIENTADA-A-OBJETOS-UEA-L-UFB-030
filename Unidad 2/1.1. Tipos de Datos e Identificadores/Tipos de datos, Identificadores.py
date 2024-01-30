# Programa para gestionar registro de productos de una Empresa de Lácteos
#He usado tipos de datos como int, float, bool y str para representar apropiadamente los datos de un registro de un producto lácteo.
#Los nombres de variables y función siguen la convención snake_case.




# Variables con datos del producto
id_producto = 202024 # int
Nombre = "Queso Mozzarella" # str
Precio_unidad =5.5 # float
Unidades_en_stock = 100 # int
Requiere_refrigeracion = True #bool
Fecha_ingreso = "2023-12-05" # str en formato AAAA-MM-DD

# Función para imprimir datos del registro
def imprimir_registro(id_prod, Nombre, Precio, Unidades, Refrigeracion, Fecha):
    print(f"ID Producto: {id_prod}")
    print(f"Nombre Producto: {Nombre}")
    print(f"Precio por Unidad: {Precio}")
    print(f"Unidades en Stock: {Unidades}")
    print(f"¿Requiere Refrigeración?: {Refrigeracion}")
    print(f"Fecha de Ingreso: {Fecha}")

# Llamada a la función para imprimir datos
imprimir_registro(id_producto, Nombre, Precio_unidad, Unidades_en_stock, Requiere_refrigeracion, Fecha_ingreso)