# Se crea una Aplicación GUI de Lista de Tareas, para que el usuario pueda agregar, marcar como completada, desmarcar y eliminar tareas de una lista de tareas utilizando botones y campos de entrada en Tkinter.
# Se importan los módulos necesarios de Tkinter: tk para la creación de ventanas y widgets, y messagebox para mostrar mensajes emergentes.
# Se define una clase llamada TodoApp. Esta clase es responsable de crear y manejar la interfaz de usuario de la aplicación.
# En el método __init__, se inicializa la ventana principal (root) y se configura el título de la ventana.
# Se crea una lista vacía llamada tasks para almacenar las tareas.
# El método create_widgets se encarga de crear y configurar los diferentes widgets de la interfaz de usuario, como etiquetas, campos de entrada, botones y un Listbox para mostrar la lista de tareas.
# El método add_task se llama cuando se hace clic en el botón "Añadir Tarea".
# Los métodos complete_task, uncomplete_task y delete_task se llaman cuando se hace clic en los botones correspondientes.
# Se crea una instancia de la clase TodoApp con la ventana principal root y se inicia el bucle principal (mainloop) para que la aplicación se ejecute.


import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        # Crear una lista vacía para almacenar las tareas
        self.tasks = []

        # Crear la interfaz gráfica de usuario
        self.create_widgets()

    def create_widgets(self):
        # Etiqueta y campo de entrada para el nombre de la tarea
        self.new_task_label = tk.Label(self.root, text="")
        self.new_task_label.pack(pady=5)
        self.new_task_entry = tk.Entry(self.root, width=50)
        self.new_task_entry.pack(pady=5)

        # Botón para añadir tarea
        self.add_task_button = tk.Button(self.root, text="Añadir Tarea", command=self.add_task)
        self.add_task_button.pack(pady=5)
        # Etiqueta y campo de entrada para la descripción de la tarea
        self.task_desc_label = tk.Label(self.root, text="Descripción:")
        self.task_desc_label.pack(pady=5)
        self.task_desc_entry = tk.Text(self.root, width=50, height=5)

        # Lista de tareas utilizando un Listbox
        self.tasks_listbox = tk.Listbox(self.root, width=50, height=10)
        self.tasks_listbox.pack(pady=10)

        # Botón para marcar tarea como completada
        self.complete_task_button = tk.Button(self.root, text="Marcar como Completada", command=self.complete_task)
        self.complete_task_button.pack(pady=5)

        # Botón para desmarcar tarea como completada
        self.uncomplete_task_button = tk.Button(self.root, text="Desmarcar Tarea", command=self.uncomplete_task)
        self.uncomplete_task_button.pack(pady=5)

        # Botón para eliminar tarea
        self.delete_task_button = tk.Button(self.root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_task_button.pack(pady=5)

        # Manejar el evento de presionar Enter en la entrada de texto
        self.new_task_entry.bind("<Return>", lambda event: self.add_task())

    def add_task(self):
        new_task_name = self.new_task_entry.get()
        new_task_desc = self.task_desc_entry.get("1.0", tk.END).strip()  # Obtener la descripción de la tarea
        if new_task_name:
            self.tasks.append({"name": new_task_name, "description": new_task_desc, "completed": False})
            self.tasks_listbox.insert(tk.END, new_task_name)
            self.new_task_entry.delete(0, tk.END)  # Limpiar el campo de entrada
            self.task_desc_entry.delete("1.0", tk.END)  # Limpiar el campo de descripción

    def complete_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            task = self.tasks[task_index]
            if not task["completed"]:
                task["completed"] = True
                self.tasks_listbox.itemconfig(task_index, bg="light green")  # Cambiar color de la tarea completada

    def uncomplete_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            task = self.tasks[task_index]
            if task["completed"]:
                task["completed"] = False
                self.tasks_listbox.itemconfig(task_index, bg=self.root.cget("bg"))  # Cambiar color de la tarea no completada

    def delete_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            del self.tasks[task_index]  # Eliminar tarea de la lista
            self.tasks_listbox.delete(task_index)  # Eliminar tarea de la lista gráfica

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
