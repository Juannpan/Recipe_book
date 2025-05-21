import tkinter as tk
from tkinter import messagebox
from backend import recipe, recipe_manager  # Asumiendo que guardaste las clases en este archivo

class RecetasApp:
    def __init__(self, root):
        self.root = root
        self.manager = recipe_manager('recetas.csv')
        self.setup_ui()
        
    def setup_ui(self):
        self.root.title('Registrar recetas')
        self.root.geometry('400x400')
        self.root.configure(bg="#fff8f0")
        
        # Configuración de grid (igual que tu versión original)
        self.root.columnconfigure(0, weight=1)
        for i in range(8):
            self.root.grid_rowconfigure(i, weight=2 if i > 0 else 3)
        
        # Widgets (adaptados para usar el manager)
        tk.Label(self.root, text='RECETAS', font=("Mongolian Baiti", 16, "bold"), bg="#fff8f0").grid(row=0, column=0)
        tk.Label(self.root, text='Crea, registra y guarda tu receta', font=("Mongolian Baiti", 10), bg="#fff8f0").grid(row=1, column=0)
        
        tk.Button(self.root, text='Registrar receta', font=("Mongolian Baiti", 10), 
                 command=self.open_input_window, bg="#4a90e2", fg="#ffffff").grid(row=2, column=0, sticky='nsew', padx=3, pady=3)
        
        tk.Button(self.root, text='Ver receta', font=("Mongolian Baiti", 10), 
                 command=self.ver_receta, bg="#4a90e2", fg="#ffffff").grid(row=3, column=0, sticky='nsew', padx=3, pady=3)
        
        self.index_entry = tk.Entry(self.root)
        self.index_entry.grid(row=4, column=0)
        
        tk.Button(self.root, text='Eliminar receta', font=("Mongolian Baiti", 10), 
                 command=self.eliminar_receta, bg="#4a90e2", fg="#ffffff").grid(row=5, column=0, sticky='nsew', padx=3, pady=3)
        
        tk.Button(self.root, text='Guardar archivo receta', font=("Mongolian Baiti", 10), 
                 bg="#4a90e2", fg="#ffffff").grid(row=7, column=0, sticky='nsew', padx=3, pady=3)

    def open_input_window(self):
        input_window = tk.Toplevel(self.root)
        input_window.title("Agregar Receta")
        input_window.geometry("300x200")
        
        tk.Label(input_window, text="Nombre de la receta:").pack(pady=5)
        self.name_entry = tk.Entry(input_window, width=40)
        self.name_entry.pack(pady=5)
        
        tk.Label(input_window, text="Tiempo de cocción (min):").pack(pady=5)
        self.time_entry = tk.Entry(input_window, width=40)
        self.time_entry.pack(pady=5)
        
        tk.Label(input_window, text="Temperatura (°C):").pack(pady=5)
        self.temp_entry = tk.Entry(input_window, width=40)
        self.temp_entry.pack(pady=5)
        
        tk.Button(input_window, text="Agregar", command=self.add_recipe).pack(pady=5)
        tk.Button(input_window, text="Cerrar", command=input_window.destroy).pack()

    def add_recipe(self):
        name = self.name_entry.get()
        time = int(self.time_entry.get())
        temp = int(self.temp_entry.get())
        
        new_recipe = recipe(
            id_receta=self.manager.get_last_id() + 1,
            cooking_time=time,
            recipe_name=name,
            recipe_degrees=temp
        )
        self.manager.save_recipe(new_recipe)
        tk.messagebox.showinfo("Éxito", "Receta agregada correctamente")

    def ver_receta(self):
        try:
            idx = int(self.index_entry.get())
            recipe_data = self.manager.id_by_recipe(idx)
            
            if recipe_data:
                top = tk.Toplevel(self.root)
                top.title(f"Receta #{idx}")
                top.geometry("300x200")
                
                labels = ['ID', 'Nombre', 'Tiempo (min)', 'Temp. (C)', 'Temp. (F)']
                for i, (label, value) in enumerate(zip(labels, recipe_data)):
                    tk.Label(top, text=f"{label}: {value}").pack(anchor="w", padx=10, pady=2)
            else:
                tk.messagebox.showerror("Error", "Receta no encontrada")
        except ValueError:
            tk.messagebox.showerror("Error", "Por favor ingresa un ID válido")

    def eliminar_receta(self):
        # Implementar lógica de eliminación similar a ver_receta
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = RecetasApp(root)
    root.mainloop()