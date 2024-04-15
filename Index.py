from tkinter import Tk, Label
from PIL import Image, ImageTk
from customtkinter import *
# Crear la ventana principal
root = CTk()
root.title("Interfaz con Imágenes y Texto")

# Cargar las imágenes
imagen_empleado = Image.open("Empleado.png")
imagen_empleado = imagen_empleado.resize((200, 200))
imagen_empleado = ImageTk.PhotoImage(imagen_empleado)

imagen_encargado = Image.open("Encargado.png")
imagen_encargado = imagen_encargado.resize((200, 200))
imagen_encargado = ImageTk.PhotoImage(imagen_encargado)

# Crear etiquetas para mostrar las imágenes
label_empleado = Label(root, image=imagen_empleado)
label_encargado = Label(root, image=imagen_encargado)

# Crear etiquetas de texto para empleado y encargado
texto_empleado = Label(root, text="Empleado", font=("Arial", 12))
texto_encargado = Label(root, text="Encargado", font=("Arial", 12))

# Colocar las etiquetas en la ventana
label_empleado.grid(row=0, column=0, padx=10, pady=10)
label_encargado.grid(row=0, column=1, padx=10, pady=10)
texto_empleado.grid(row=1, column=0)
texto_encargado.grid(row=1, column=1)

root.mainloop()
