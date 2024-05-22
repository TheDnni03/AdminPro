import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import psycopg2
from ttkthemes import ThemedStyle
from Conexion import conectar_bd

def insertar_datos():
    usuario = entry_usuario.get()
    nombre = entry_nombre.get()
    apellido_paterno = entry_apellido_paterno.get()
    apellido_materno = entry_apellido_materno.get()
    password = entry_password.get()
    rol = 1

    try:
        conexion = conectar_bd()
        if conexion is None:
            raise psycopg2.DatabaseError("No se pudo conectar a la base de datos")

        cur = conexion.cursor()
        cur.execute("INSERT INTO Usuario(Usuario, Nombre, Apellido1, Apellido2, Password, Tipo) VALUES (%s, %s, %s, %s, %s, %s);", 
            (usuario, nombre, apellido_paterno, apellido_materno, password, rol))
        conexion.commit()
        messagebox.showinfo("Éxito", "Inserción exitosa.")
        cur.close()
        conexion.close()
    except (Exception, psycopg2.DatabaseError) as error:
        messagebox.showerror("Error", f"Error al insertar: {error}")

ventana = tk.Tk()
ventana.title("Interfaz de Inserción de Datos")
ventana.geometry('300x300')

style = ThemedStyle(ventana)
style.set_theme("plastik")

label_usuario = ttk.Label(ventana, text="Usuario:")
label_usuario.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
entry_usuario = ttk.Entry(ventana)
entry_usuario.grid(row=0, column=1, padx=10, pady=5)

label_nombre = ttk.Label(ventana, text="Nombre:")
label_nombre.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
entry_nombre = ttk.Entry(ventana)
entry_nombre.grid(row=1, column=1, padx=10, pady=5)

label_apellido_paterno = ttk.Label(ventana, text="Apellido Paterno:")
label_apellido_paterno.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
entry_apellido_paterno = ttk.Entry(ventana)
entry_apellido_paterno.grid(row=2, column=1, padx=10, pady=5)

label_apellido_materno = ttk.Label(ventana, text="Apellido Materno:")
label_apellido_materno.grid(row=3, column=0, padx=10, pady=5, sticky=tk.E)
entry_apellido_materno = ttk.Entry(ventana)
entry_apellido_materno.grid(row=3, column=1, padx=10, pady=5)

label_password = ttk.Label(ventana, text="Contraseña:")
label_password.grid(row=4, column=0, padx=10, pady=5, sticky=tk.E)
entry_password = ttk.Entry(ventana, show="*")
entry_password.grid(row=4, column=1, padx=10, pady=5)

btn_insertar = ttk.Button(ventana, text="Insertar Datos", command=insertar_datos)
btn_insertar.grid(row=5, columnspan=2, padx=10, pady=10)
ventana.mainloop()