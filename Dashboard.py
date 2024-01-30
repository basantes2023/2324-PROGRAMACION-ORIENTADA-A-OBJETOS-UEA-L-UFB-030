import os


def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'Unidad 1/1.2. Técnicas de programación/Encapsulación.py',
        '2': 'Unidad 1/1.2. Técnicas de programación/Herencia.py',
        '3': 'Unidad 1/1.2. Técnicas de programación/abstracción.py',
        '4': 'Unidad 1/1.2. Técnicas de programación/polimorfismo.py',
        '5': 'Unidad 1/2.1. Programación tradicional frente a POO/Temperatura P. Tradicional.py',
        '6': 'Unidad 1/2.1. Programación tradicional frente a POO/Temperatura POO.py',
        '7': 'Unidad 1/2.2. Características de la POO/Reservas Pasajes Aéreos.py',
        '8': 'Unidad 1/2.2. Características de la POO/Sistema de Gestión de Empleados.py',
        '9': 'Unidad 1/2.2. Características de la POO/TiendaOnline.py',
        '10': 'Unidad 2/1.1. Tipos de Datos e Identificadores/Tipos de datos, Identificadores.py',
        '11': 'Unidad 2/1.2. Clases, Objetos, Herencia, Encapsulamiento y Polimorfismo/_APLIC~1.PY',
        '12': 'Unidad 2/2.1. Constructores y Destructores/Implementación de Constructores y Destructores.py',
               
        
            }

    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
