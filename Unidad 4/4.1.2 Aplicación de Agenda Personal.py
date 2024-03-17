# Se crea una aplicación de agenda personal con una interfaz gráfica donde el usuario puede agregar, eliminar, visualizar eventos y gestionando las interacciones con el usuario mediante funciones específicas para cada acción.
# El código importa los módulos necesarios para la interfaz gráfica, como tkinter para la creación de ventanas y widgets, ttk para estilos mejorados de widgets, messagebox para mostrar mensajes emergentes y tkcalendar para el widget de calendario.
# Se define una clase AgendaApp que representa la aplicación de agenda personal. Esta clase contiene métodos para la funcionalidad principal de la aplicación, como agregar eventos y eliminar eventos seleccionados.
# En el método __init__, se crea la ventana principal (root) y se configura el título de la aplicación. También se crean y empaquetan los frames para la lista de eventos (frame_list) y la entrada de datos (frame_inputs).
# Se utiliza un Treeview (self.tree) para mostrar la lista de eventos, con columnas para la fecha, hora y descripción. Se configuran las columnas y encabezados del Treeview.
# Se crean etiquetas (lbl_fecha, lbl_hora, lbl_descripcion) y campos de entrada (entry_fecha, entry_hora, entry_descripcion) para que el usuario pueda ingresar la fecha, hora y descripción del evento.
# Se crean botones (btn_agregar, btn_eliminar, btn_salir) para agregar eventos, eliminar eventos seleccionados y salir de la aplicación, respectivamente. Se vinculan estos botones con funciones para ejecutar acciones cuando se hace clic en ellos.
# Se definen las funciones agregar_evento y eliminar_evento para manejar la lógica de agregar eventos nuevos y eliminar eventos seleccionados del Treeview. Se valida que todos los campos estén llenos antes de agregar un evento y se muestra un mensaje de advertencia si alguno está vacío.
# Se crea una instancia de la clase AgendaApp y se inicia el ciclo principal de la interfaz gráfica con root.mainloop().


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar

class AgendaApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Agenda Personal")

        # Frame para mostrar la lista de eventos
        self.frame_list = tk.Frame(self.root)
        self.frame_list.pack(pady=10)

        # Treeview para mostrar la lista de eventos
        self.tree = ttk.Treeview(self.frame_list, columns=("Fecha", "Hora", "Descripción"), selectmode="browse")
        self.tree.heading("#0", text="ID")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack()

        # Frame para la entrada de datos
        self.frame_inputs = tk.Frame(self.root)
        self.frame_inputs.pack(pady=5)

        # Etiquetas y campos de entrada para la fecha, hora y descripción
        self.lbl_fecha = tk.Label(self.frame_inputs, text="Fecha:")
        self.lbl_fecha.grid(row=0, column=0, padx=5)
        self.entry_fecha = Calendar(self.frame_inputs, selectmode='day', year=2024, month=3, day=16)
        self.entry_fecha.grid(row=0, column=1, padx=5)

        self.lbl_hora = tk.Label(self.frame_inputs, text="Hora:")
        self.lbl_hora.grid(row=0, column=2, padx=5)
        self.entry_hora = tk.Entry(self.frame_inputs)
        self.entry_hora.grid(row=0, column=3, padx=5)

        self.lbl_descripcion = tk.Label(self.frame_inputs, text="Descripción:")
        self.lbl_descripcion.grid(row=1, column=0, padx=5)
        self.entry_descripcion = tk.Entry(self.frame_inputs, width=50)
        self.entry_descripcion.grid(row=1, column=1, columnspan=3, padx=5)

        # Botones para agregar, eliminar eventos y salir
        self.btn_agregar = tk.Button(self.frame_inputs, text="Agregar Evento", command=self.agregar_evento)
        self.btn_agregar.grid(row=2, column=0, pady=5)

        self.btn_eliminar = tk.Button(self.frame_inputs, text="Eliminar Evento Seleccionado", command=self.eliminar_evento)
        self.btn_eliminar.grid(row=2, column=1, pady=5)

        self.btn_salir = tk.Button(self.frame_inputs, text="Salir", command=root.quit)
        self.btn_salir.grid(row=2, column=2, pady=5)

    def agregar_evento(self):
        # Obtener los datos de los campos de entrada
        fecha = self.entry_fecha.get_date()
        hora = self.entry_hora.get()
        descripcion = self.entry_descripcion.get()
        # Verificar que todos los campos estén llenos
        if fecha and hora and descripcion:
            # Insertar el evento en el Treeview
            self.tree.insert("", "end", text="Evento", values=(fecha, hora, descripcion))
            # Limpiar los campos de entrada después de agregar el evento
            self.entry_hora.delete(0, tk.END)
            self.entry_descripcion.delete(0, tk.END)
        else:
            # Mostrar un mensaje de advertencia si algún campo está vacío
            messagebox.showwarning("Error", "Por favor, complete todos los campos.")

    def eliminar_evento(self):
        # Obtener el evento seleccionado en el Treeview
        selected_item = self.tree.selection()
        if selected_item:
            # Mostrar un mensaje de confirmación antes de eliminar el evento
            if messagebox.askyesno("Eliminar Evento", "¿Estás seguro de que quieres eliminar este evento?"):
                # Eliminar el evento seleccionado
                self.tree.delete(selected_item)
        else:
            # Mostrar un mensaje de advertencia si no se ha seleccionado ningún evento
            messagebox.showwarning("Error", "Por favor, selecciona un evento para eliminar.")

if _name_ == "_main_":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
