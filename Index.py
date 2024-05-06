import tkinter as tk
from PIL import Image, ImageTk 
import psycopg2
import subprocess

usuario_seleccionado = None

def seleccionar_usuario(usuario):
    global usuario_seleccionado
    usuario_seleccionado = usuario
    if usuario == "Empleado":
        subprocess.Popen(["python", "RegEmpleado.py"])
    elif usuario == "Encargado":
        subprocess.Popen(["python", "RegEncargado.py"])
    ventana.destroy()  # Destruir la ventana principal después de abrir la siguiente ventana

ventana = tk.Tk()
ventana.title("Inicio")
ventana.geometry("500x300")

contenedor_imagenes = tk.Frame(ventana)
contenedor_imagenes.pack()

espacio_superior = tk.Label(contenedor_imagenes, height=4)
espacio_superior.pack()

frame_imagen_texto1 = tk.Frame(contenedor_imagenes)
frame_imagen_texto1.pack(side=tk.LEFT, padx=20)  

imagen1 = Image.open("Empleado.png")
imagen1 = imagen1.resize((100, 100))  
imagen_tk1 = ImageTk.PhotoImage(imagen1)

label_imagen1 = tk.Label(frame_imagen_texto1, image=imagen_tk1)
label_imagen1.pack()

label_imagen1.image = imagen_tk1

label_texto1 = tk.Label(frame_imagen_texto1, text="Empleado")
label_texto1.pack()

label_imagen1.bind("<Button-1>", lambda event: seleccionar_usuario("Empleado"))

espacio = tk.Label(contenedor_imagenes, width=10)
espacio.pack(side=tk.LEFT)

frame_imagen_texto2 = tk.Frame(contenedor_imagenes)
frame_imagen_texto2.pack(side=tk.LEFT, padx=20)  

imagen2 = Image.open("Encargado.png")
imagen2 = imagen2.resize((100, 100))  
imagen_tk2 = ImageTk.PhotoImage(imagen2)

label_imagen2 = tk.Label(frame_imagen_texto2, image=imagen_tk2)
label_imagen2.pack()

label_imagen2.image = imagen_tk2

label_texto2 = tk.Label(frame_imagen_texto2, text="Encargado")
label_texto2.pack()

label_imagen2.bind("<Button-1>", lambda event: seleccionar_usuario("Encargado"))

ventana.mainloop()

