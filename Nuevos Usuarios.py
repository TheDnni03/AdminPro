import tkinter as tk
from tkinter import messagebox
import psycopg2

def insertar_datos():
    nombre = entry_nombre.get()
    password = entry_password.get()

    try:
        conn = psycopg2.connect(
            dbname="almacen",
            user="postgres",
            password="D11Z08V03",
            host="localhost",
            port="5432"
        )

        cur = conn.cursor()
        cur.execute("INSERT INTO Usuarios (Nombre, Password) VALUES (%s, %s);", (nombre, password))
        conn.commit()
        messagebox.showinfo("Éxito", "Inserción exitosa.")
        cur.close()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        messagebox.showerror("Error", "Error al insertar: {}".format(error))

# Crear ventana
ventana = tk.Tk()
ventana.title("Interfaz de Inserción de Datos")

# Etiquetas y campos de entrada
label_nombre = tk.Label(ventana, text="Nombre:")
label_nombre.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1, padx=10, pady=5)

label_password = tk.Label(ventana, text="Contraseña:")
label_password.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
entry_password = tk.Entry(ventana, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=5)

# Botón de inserción
btn_insertar = tk.Button(ventana, text="Insertar Datos", command=insertar_datos)
btn_insertar.grid(row=2, columnspan=2, padx=10, pady=10)

# Ejecutar ventana
ventana.mainloop()
