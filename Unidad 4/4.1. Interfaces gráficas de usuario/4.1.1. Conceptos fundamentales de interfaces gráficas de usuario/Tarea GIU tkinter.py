# Sistema de una Aplicación GUI Básica
# Creamos una clase GUIApp que representa nuestra aplicación de interfaz gráfica.
# En el método __init__(), creamos y configuramos los diferentes componentes de la interfaz, como etiquetas, campos de texto, botones y una lista para mostrar los datos.
# El botón "Agregar" llama al método add_info() cuando se hace clic en él. Este método recupera la información ingresada en el campo de texto, la agrega a la lista y luego borra el contenido del campo de texto.
# El botón "Limpiar" llama al método clear_info() cuando se hace clic en él. Este método borra todos los elementos de la lista.
# El método run() inicia el bucle principal de la aplicación.


import tkinter as tk


class GUIApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Aplicación GUI Básica")

        # Etiqueta
        self.label = tk.Label(self.window, text="Ingrese información:")
        self.label.pack()

        # Campo de texto
        self.entry = tk.Entry(self.window)
        self.entry.pack()

        # Botón Agregar
        self.add_button = tk.Button(self.window, text="Agregar", command=self.add_info)
        self.add_button.pack()

        # Lista para mostrar datos
        self.listbox = tk.Listbox(self.window)
        self.listbox.pack()

        # Botón Limpiar
        self.clear_button = tk.Button(self.window, text="Limpiar", command=self.clear_info)
        self.clear_button.pack()

    def add_info(self):
        info = self.entry.get()
        self.listbox.insert(tk.END, info)
        self.entry.delete(0, tk.END)

    def clear_info(self):
        self.listbox.delete(0, tk.END)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = GUIApp()
    app.run()
