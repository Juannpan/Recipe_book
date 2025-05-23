import tkinter as tk
from tkinter import messagebox
from backend import recipe, recipe_manager

class RecetasApp:
    def __init__(self, root):
        self.root = root
        self.manager = recipe_manager('recetas.csv')
        self.setup_ui()
    
    def setup_ui(self):
        self.root.title('Registrar recetas')
        self.root.geometry('400x400')
        self.root.configure(bg="#fff8f0")
        
        # Configuración de grid
        self.root.columnconfigure(0, weight=1)
        for i in range(8):
            self.root.grid_rowconfigure(i, weight=2 if i > 0 else 3)
        
        # Widgets
        tk.Label(self.root, text='RECETAS', font=("Mongolian Baiti", 16, "bold"), bg="#fff8f0").grid(row=0, column=0)
        tk.Label(self.root, text='Crea, registra y guarda tu receta', font=("Mongolian Baiti", 10), bg="#fff8f0").grid(row=1, column=0)
        
        tk.Button(self.root, text='Registrar receta', font=("Mongolian Baiti", 10), 
                 command=self.open_input_window, bg="#4a90e2", fg="#ffffff").grid(row=2, column=0, sticky='nsew', padx=3, pady=3)
        
        tk.Button(self.root, text='Ver receta', font=("Mongolian Baiti", 10), 
                 command=self.view_recipe, bg="#4a90e2", fg="#ffffff").grid(row=3, column=0, sticky='nsew', padx=3, pady=3)
        
        self.id_entry = tk.Entry(self.root)
        self.id_entry.grid(row=4, column=0)
        
        tk.Button(self.root, text='Eliminar receta', font=("Mongolian Baiti", 10), 
                 command=self.delete_recipe, bg="#4a90e2", fg="#ffffff").grid(row=5, column=0, sticky='nsew', padx=3, pady=3)
        
        tk.Button(self.root, text='Guardar archivo receta', font=("Mongolian Baiti", 10), 
                 bg="#4a90e2", fg="#ffffff").grid(row=7, column=0, sticky='nsew', padx=3, pady=3)
    
    def open_input_window(self):
        """Ventana para ingresar nueva receta"""
        self.input_win = tk.Toplevel(self.root)
        self.input_win.title("Agregar Receta")
        self.input_win.geometry("300x200")
        
        # Nombre
        tk.Label(self.input_win, text="Nombre de la receta:").pack(pady=5)
        self.name_entry = tk.Entry(self.input_win, width=30)
        self.name_entry.pack(pady=5)
        
        # Temperatura
        tk.Label(self.input_win, text="Temperatura (°C):").pack(pady=5)
        self.temp_entry = tk.Entry(self.input_win, width=30)
        self.temp_entry.pack(pady=5)
        
        # Botones
        tk.Button(self.input_win, text="Agregar", command=self.add_recipe).pack(pady=10)
        tk.Button(self.input_win, text="Cerrar", command=self.input_win.destroy).pack()
    
    def add_recipe(self):
        """Agrega una nueva receta al sistema"""
        try:
            name = self.name_entry.get()
            temp = int(self.temp_entry.get())
            
            if not name:
                raise ValueError("El nombre no puede estar vacío")
            if temp <= 0:
                raise ValueError("La temperatura debe ser positiva")
            
            new_recipe = recipe(
                id_receta=self.manager.get_last_id() + 1,
                recipe_name=name,
                recipe_degrees=temp
            )
            
            self.manager.save_recipe(new_recipe)
            messagebox.showinfo("Éxito", f"Receta agregada:\nNombre: {name}\nTiempo: {new_recipe.time} min\nTemp: {temp}°C ({new_recipe.fdegrees}°F)")
            self.input_win.destroy()
            
        except ValueError as e:
            messagebox.showerror("Error", f"Datos inválidos: {str(e)}")
    
    def view_recipe(self):
        """Muestra los detalles de una receta"""
        try:
            recipe_id = int(self.id_entry.get())
            recipe_data = self.manager.get_recipe_by_id(recipe_id)
            
            if recipe_data:
                view_win = tk.Toplevel(self.root)
                view_win.title(f"Receta #{recipe_id}")
                view_win.geometry("300x200")
                
                labels = ['ID', 'Nombre', 'Tiempo (min)', 'Temp. (C)', 'Temp. (F)']
                for label, value in zip(labels, recipe_data):
                    tk.Label(view_win, text=f"{label}: {value}", anchor="w").pack(fill='x', padx=10, pady=2)
            else:
                messagebox.showerror("Error", "Receta no encontrada")
                
        except ValueError:
            messagebox.showerror("Error", "Ingresa un ID válido (número)")
    
    def delete_recipe(self):
        """Elimina una receta del sistema"""
        try:
            recipe_id = int(self.id_entry.get())
            recipes = self.manager.get_all_recipes()
            
            updated_recipes = [r for r in recipes if r[0] != str(recipe_id)]
            
            with open(self.manager.filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['ID', 'Nombre', 'Tiempo (min)', 'Temp. (C)', 'Temp. (F)'])
                writer.writerows(updated_recipes)
            
            messagebox.showinfo("Éxito", f"Receta #{recipe_id} eliminada")
            
        except ValueError:
            messagebox.showerror("Error", "Ingresa un ID válido (número)")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo eliminar: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RecetasApp(root)
    root.mainloop()