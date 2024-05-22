import tkinter as tk
import os
import psycopg2
from Conexion import conectar_bd

def verificar_usuario():
    nombre = entry_nombre.get()
    contraseña = entry_contraseña.get()
    conexion = conectar_bd()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM Usuario WHERE Usuario = %s AND Password = %s", (nombre, contraseña))
            resultado = cursor.fetchone()
            if resultado:
                label_resultado.config(text="Usuario encontrado en la base de datos.")
                ventana.destroy()
                os.system("python VentanaEmpleado.py")
            else:
                label_resultado.config(text="Usuario no encontrado en la base de datos.")
        except psycopg2.Error as error:
            print("Error al conectar a la base de datos:", error)
            label_resultado.config(text="Error al conectar a la base de datos.")
        finally:
            conexion.close()

# Crear la ventana
ventana = tk.Tk()
ventana.title("Verificar Usuario")
ventana.geometry("800x400")

# Etiqueta y campo de entrada para el nombre
label_nombre = tk.Label(ventana, text="Nombre:")
label_nombre.pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

label_contraseña = tk.Label(ventana, text="Contraseña:")
label_contraseña.pack()
entry_contraseña = tk.Entry(ventana, show="*")
entry_contraseña.pack()

boton_verificar = tk.Button(ventana, text="Verificar Usuario", command=verificar_usuario)
boton_verificar.pack()

label_resultado = tk.Label(ventana, text="")
label_resultado.pack()

ventana.mainloop()