import tkinter as tk


def open_input_window():
    input_window = tk.Toplevel(root)
    input_window.title("Agregar Receta")
    input_window.geometry("300x150")

    tk.Label(input_window, text="Escribe algo:").pack(pady=5)
    entry = tk.Entry(input_window, width=40)
    entry.pack(pady=5)

 
    def add_text():
        typed_text = entry.get()
        print("Texto agregado:", typed_text)

    add_button = tk.Button(input_window, text="Agregar", command=add_text)
    add_button.pack(pady=5)

    close_button = tk.Button(input_window, text="Cerrar", command=input_window.destroy)
    close_button.pack()



root = tk.Tk()

root.title('Registrar recetas')
root.geometry('400x400')
root.columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=3)
root.grid_rowconfigure(1, weight=2)
root.grid_rowconfigure(2, weight=2)
root.grid_rowconfigure(3, weight=2)
root.grid_rowconfigure(4, weight=2)
root.grid_rowconfigure(5, weight=2)
root.grid_rowconfigure(6, weight=2)
root.grid_rowconfigure(7, weight=2)

root.configure(bg="#fff8f0")

index = tk.StringVar()
def ver_receta():
    try:
        #idx = int(index.get()) 
        #if idx < 0 or idx >= len(df):
            #raise IndexError("Índice fuera de rango")

        #receta = df.iloc[idx]  

        top = tk.Toplevel(root)
        top.title(f"Receta")
        top.geometry("300x200")

        #for col, val in receta.items():
            #tk.Label(top, text=f"{col}: {val}").pack(anchor="w", padx=10, pady=2)

    except ValueError:
        print("Por favor, ingresa un número válido.")
    except IndexError as e:
        print(e)

title = tk.Label(root, text='RECETAS', font=("Mongolian Baiti", 16, "bold"), bg="#fff8f0")
title.grid(row=0, column=0)

title = tk.Label(root, text='Crea, registra y guarda tu receta', font=("Mongolian Baiti", 10), bg="#fff8f0")
title.grid(row=1, column=0)

registrar_receta = tk.Button(text='Registrar receta', font=("Mongolian Baiti", 10), command=open_input_window, bg="#4a90e2", fg="#ffffff")
registrar_receta.grid(row=2, column=0, sticky='nsew', padx=3, pady=3)

ver_recetas = tk.Button(text='Ver receta', font=("Mongolian Baiti", 10), command=ver_receta, bg="#4a90e2", fg="#ffffff")
ver_recetas.grid(row=3, column=0, sticky='nsew', padx=3, pady=3)
entry = tk.Entry(root, textvariable=index)
entry.grid(row=4, column=0)

eliminar_receta = tk.Button(text='Eliminar receta', font=("Mongolian Baiti", 10), bg="#4a90e2", fg="#ffffff")
eliminar_receta.grid(row=5, column=0, sticky='nsew', padx=3, pady=3)
entry2 = tk.Entry(root, textvariable=index)
entry2.grid(row=6, column=0)

guardar_archivo = tk.Button(text='Guardar archivo receta', font=("Mongolian Baiti", 10), bg="#4a90e2", fg="#ffffff")
guardar_archivo.grid(row=7, column=0, sticky='nsew', padx=3, pady=3)

root.mainloop()
