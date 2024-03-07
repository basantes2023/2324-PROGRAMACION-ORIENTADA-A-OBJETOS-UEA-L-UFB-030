#Sistema de Gestión de Biblioteca Digital
#Este programa implementa las clases Libro, Usuario y Biblioteca para gestionar la biblioteca digital,
# Posee una interfaz de línea de comandos que permite al usuario interactuar con el sistema. Se utilizan listas, tuplas, diccionarios y conjuntos según los requisitos especificados.
# Además, se incluyen comentarios para explicar la lógica detrás de las decisiones de implementación y se prueban varias operaciones del sistema de biblioteca a través de la interfaz de usuario.


class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo_autor = (titulo, autor)  # Utilizamos una tupla para título y autor
        self.categoria = categoria
        self.isbn = isbn


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista para gestionar libros prestados


class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # Diccionario para almacenar libros por ISBN
        self.usuarios_registrados = set()  # Conjunto para IDs de usuarios únicos

    def agregar_libro(self, libro):
        self.libros_disponibles[libro.isbn] = libro

    def quitar_libro(self, isbn):
        del self.libros_disponibles[isbn]

    def registrar_usuario(self, usuario):
        self.usuarios_registrados.add(usuario.id_usuario)

    def dar_de_baja_usuario(self, id_usuario):
        self.usuarios_registrados.remove(id_usuario)

    def prestar_libro(self, libro, usuario):
        if libro.isbn in self.libros_disponibles and usuario.id_usuario in self.usuarios_registrados:
            usuario.libros_prestados.append(libro)
            del self.libros_disponibles[libro.isbn]
            print(f"Libro '{libro.titulo_autor[0]}' prestado a {usuario.nombre}.")
        else:
            print("Libro no disponible o usuario no registrado.")

    def devolver_libro(self, libro, usuario):
        if libro in usuario.libros_prestados:
            self.libros_disponibles[libro.isbn] = libro
            usuario.libros_prestados.remove(libro)
            print(f"Libro '{libro.titulo_autor[0]}' devuelto por {usuario.nombre}.")
        else:
            print("Este usuario no tiene prestado este libro.")

    def buscar_libro_por_titulo(self, titulo):
        libros_encontrados = [libro for libro in self.libros_disponibles.values() if titulo.lower() in libro.titulo_autor[0].lower()]
        return libros_encontrados

    def buscar_libro_por_autor(self, autor):
        libros_encontrados = [libro for libro in self.libros_disponibles.values() if autor.lower() in libro.titulo_autor[1].lower()]
        return libros_encontrados

    def buscar_libro_por_categoria(self, categoria):
        libros_encontrados = [libro for libro in self.libros_disponibles.values() if categoria.lower() == libro.categoria.lower()]
        return libros_encontrados

    def listar_libros_prestados(self, usuario):
        if usuario.libros_prestados:
            print(f"Libros prestados a {usuario.nombre}:")
            for libro in usuario.libros_prestados:
                print(f"  - '{libro.titulo_autor[0]}' por {libro.titulo_autor[1]}")
        else:
            print(f"{usuario.nombre} no tiene libros prestados.")


# Interfaz de línea de comandos
def menu_principal():
    print("Bienvenido a la biblioteca digital")
    print("1. Registrar usuario")
    print("2. Dar de baja usuario")
    print("3. Añadir libro")
    print("4. Quitar libro")
    print("5. Prestar libro")
    print("6. Devolver libro")
    print("7. Buscar libro")
    print("8. Listar libros prestados")
    print("9. Salir")


def ejecutar_programa():
    biblioteca = Biblioteca()

    while True:
        menu_principal()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del usuario: ")
            id_usuario = input("ID del usuario: ")
            usuario = Usuario(nombre, id_usuario)
            biblioteca.registrar_usuario(usuario)
            print("Usuario registrado correctamente.")

        elif opcion == "2":
            id_usuario = input("ID del usuario a dar de baja: ")
            biblioteca.dar_de_baja_usuario(id_usuario)
            print("Usuario dado de baja correctamente.")

        elif opcion == "3":
            titulo = input("Título del libro: ")
            autor = input("Autor del libro: ")
            categoria = input("Categoría del libro: ")
            isbn = input("ISBN del libro: ")
            libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.agregar_libro(libro)
            print("Libro añadido correctamente.")

        elif opcion == "4":
            isbn = input("ISBN del libro a quitar: ")
            biblioteca.quitar_libro(isbn)
            print("Libro quitado correctamente.")

        elif opcion == "5":
            isbn = input("ISBN del libro a prestar: ")
            id_usuario = input("ID del usuario: ")
            libro = biblioteca.libros_disponibles.get(isbn)
            usuario = Usuario("", id_usuario)  # Creamos un usuario temporal solo con el ID
            biblioteca.prestar_libro(libro, usuario)

        elif opcion == "6":
            isbn = input("ISBN del libro a devolver: ")
            id_usuario = input("ID del usuario: ")
            libro = biblioteca.libros_disponibles.get(isbn)
            usuario = Usuario("", id_usuario)  # Creamos un usuario temporal solo con el ID
            biblioteca.devolver_libro(libro, usuario)

        elif opcion == "7":
            criterio_busqueda = input("Ingrese criterio de búsqueda (titulo/autor/categoria): ").lower()
            valor = input(f"Ingrese el valor a buscar por {criterio_busqueda}: ")
            if criterio_busqueda == "titulo":
                libros_encontrados = biblioteca.buscar_libro_por_titulo(valor)
            elif criterio_busqueda == "autor":
                libros_encontrados = biblioteca.buscar_libro_por_autor(valor)
            elif criterio_busqueda == "categoria":
                libros_encontrados = biblioteca.buscar_libro_por_categoria(valor)
            else:
                print("Opción de búsqueda no válida.")
                continue

            if libros_encontrados:
                print("Libros encontrados:")
                for libro in libros_encontrados:
                    print(f"  - {libro.titulo_autor[0]} por {libro.titulo_autor[1]}")
            else:
                print("No se encontraron libros.")

        elif opcion == "8":
            id_usuario = input("ID del usuario: ")
            usuario = Usuario("", id_usuario)  # Creamos un usuario temporal solo con el ID
            biblioteca.listar_libros_prestados(usuario)

        elif opcion == "9":
            print("Gracias por usar la biblioteca digital.")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    ejecutar_programa()
