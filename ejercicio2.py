import tkinter as tk
from tkinter import messagebox

def guardar_datos():
    nombre = entry_nombre.get()
    direccion = entry_direccion.get()
    telefono = entry_telefono.get()
    
    if nombre and direccion and telefono:
        with open('registros.txt', 'a') as file:
            file.write("Nombre: {nombre}\n")
            file.write("Direccion: {direccion}\n")
            file.write("Telefono: {telefono}\n")
            file.write("-" * 40 + "\n")
            
            
        entry_nombre.delete(0, tk.END)
        entry_direccion.delete(0, tk.END)
        entry_telefono.delete(0, tk.END)
        
        messagebox.showinfo("informacion", "datos registrados")
        messagebox.showwarning("advertencia", "todos los campos son obligatorios")

#definicion de interfaz, espacio de trabajo       
root = tk.Tk()
root.title("Registradora de datos")
root.geometry("400x300")
label = tk.Label(root, text="nombre")
label.pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady = 5)
label = tk.Label(root, text="apellido")
label.pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady = 5)
label = tk.Label(root, text="direccion")
label.pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady = 5)

button = tk.Button(root, text="registrar", command=guardar_datos)
button.pack(pady= 5)
#terminar interfaz, aÃ±adir etiquetas y boton que ejecute el programa.
entry_nombre = tk.Entry(root)
entry_telefono = tk.Entry(root)
entry_direccion = tk.Entry(root)

root.mainloop()