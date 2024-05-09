import tkinter as tk
import os
from Conexion import conectar_bd

def ver_inventario():
    # Aquí puedes agregar la funcionalidad para ver el inventario
    pass

def agregar_empleado():
    # Aquí puedes agregar la funcionalidad para agregar un producto
    pass

def eliminar_empleado():
    # Aquí puedes agregar la funcionalidad para eliminar un producto
    pass

def salir():
    # Cerrar la ventana actual
    ventana.destroy()
    # Ejecutar el archivo Index.py
    os.system("python Index.py")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Encargado")
ventana.geometry("300x300")

# Botón para ver el inventario
boton_ver_inventario = tk.Button(ventana, text="Ver Inventario", command=ver_inventario)
boton_ver_inventario.pack()

# Botón para agregar un producto
boton_agregar_empleado = tk.Button(ventana, text="Agregar Producto", command=agregar_empleado)
boton_agregar_empleado.pack()

# Botón para eliminar un producto
boton_eliminar_empleado = tk.Button(ventana, text="Eliminar Producto", command=eliminar_empleado)
boton_eliminar_empleado.pack()

# Botón para salir de la aplicación
boton_salir = tk.Button(ventana, text="SALIR", command=salir)
boton_salir.pack()

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
