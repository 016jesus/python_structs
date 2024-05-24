import tkinter as tk

def mostrar_seleccion():
    # Obtener el estado de cada botón de selección y mostrarlo en la consola
    print("Opción 1:", opcion1.get())
    print("Opción 2:", opcion2.get())
    print("Opción 3:", opcion3.get())

# Crear la ventana principal
root = tk.Tk()
root.title("Botones de Selección")

# Variables de control para los botones de selección
opcion1 = tk.BooleanVar()
opcion2 = tk.BooleanVar()
opcion3 = tk.BooleanVar()

# Crear los botones de selección
check1 = tk.Checkbutton(root, text="Opción 1", variable=opcion1)
check1.pack()

check2 = tk.Checkbutton(root, text="Opción 2", variable=opcion2)
check2.pack()

check3 = tk.Checkbutton(root, text="Opción 3", variable=opcion3)
check3.pack()

# Botón para mostrar la selección
boton_mostrar = tk.Button(root, text="Mostrar selección", command=mostrar_seleccion)
boton_mostrar.pack()

# Mostrar la ventana
root.mainloop()