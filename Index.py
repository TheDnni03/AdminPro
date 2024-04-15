import tkinter as tk
from PIL import Image, ImageTk  # Importar desde el módulo PIL
import subprocess

# Variable global para almacenar el usuario seleccionado
usuario_seleccionado = None

def seleccionar_usuario(usuario):
    global usuario_seleccionado
    usuario_seleccionado = usuario
    if usuario == "Empleado":
        subprocess.Popen(["python", "Empleado.py"])
    elif usuario == "Encargado":
        subprocess.Popen(["python", "Encargado.py"])

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Inicio")  # Cambiar el título de la ventana a "Inicio"
ventana.geometry("500x300")  # Establecer el tamaño de la ventana a 300x300

# Crear un contenedor para las imágenes y textos
contenedor_imagenes = tk.Frame(ventana)
contenedor_imagenes.pack()

# Espacio en blanco en la parte superior del contenedor
espacio_superior = tk.Label(contenedor_imagenes, height=4)
espacio_superior.pack()

# Crear un frame para la primera imagen y texto
frame_imagen_texto1 = tk.Frame(contenedor_imagenes)
frame_imagen_texto1.pack(side=tk.LEFT, padx=20)  # Añadir un espacio entre los frames

# Cargar la primera imagen
imagen1 = Image.open("Empleado.png")  # Cambia "Empleado.png" por la ruta de tu primera imagen
imagen1 = imagen1.resize((100, 100))  # Redimensionar la imagen según sea necesario
imagen_tk1 = ImageTk.PhotoImage(imagen1)

# Mostrar la primera imagen en un widget Label
label_imagen1 = tk.Label(frame_imagen_texto1, image=imagen_tk1)
label_imagen1.pack()

# Guardar una referencia a la primera imagen para evitar que sea eliminada por el recolector de basura
label_imagen1.image = imagen_tk1

# Agregar un texto debajo de la primera imagen
label_texto1 = tk.Label(frame_imagen_texto1, text="Empleado")
label_texto1.pack()

# Vincular la función seleccionar_usuario con clic en la imagen 1
label_imagen1.bind("<Button-1>", lambda event: seleccionar_usuario("Empleado"))

# Crear un espacio entre las imágenes
espacio = tk.Label(contenedor_imagenes, width=10)
espacio.pack(side=tk.LEFT)

# Crear un frame para la segunda imagen y texto
frame_imagen_texto2 = tk.Frame(contenedor_imagenes)
frame_imagen_texto2.pack(side=tk.LEFT, padx=20)  # Añadir un espacio entre los frames

# Cargar la segunda imagen
imagen2 = Image.open("Encargado.png")  # Cambia "Encargado.png" por la ruta de tu segunda imagen
imagen2 = imagen2.resize((100, 100))  # Redimensionar la imagen según sea necesario
imagen_tk2 = ImageTk.PhotoImage(imagen2)

# Mostrar la segunda imagen en un widget Label
label_imagen2 = tk.Label(frame_imagen_texto2, image=imagen_tk2)
label_imagen2.pack()

# Guardar una referencia a la segunda imagen para evitar que sea eliminada por el recolector de basura
label_imagen2.image = imagen_tk2

# Agregar un texto debajo de la segunda imagen
label_texto2 = tk.Label(frame_imagen_texto2, text="Encargado")
label_texto2.pack()

# Vincular la función seleccionar_usuario con clic en la imagen 2
label_imagen2.bind("<Button-1>", lambda event: seleccionar_usuario("Encargado"))

# Iniciar el bucle de eventos principal
ventana.mainloop()

# Imprimir el usuario seleccionado después de cerrar la ventana
print("Usuario seleccionado:", usuario_seleccionado)
