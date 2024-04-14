import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import psycopg2
from ttkthemes import ThemedStyle

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

# Función para centrar la ventana
def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (300 // 2)  # Centramos respecto al ancho deseado (300)
    y = (window.winfo_screenheight() // 2) - (300 // 2)  # Centramos respecto al alto deseado (300)
    window.geometry('300x300+{}+{}'.format(x, y))

# Crear ventana
ventana = tk.Tk()
ventana.title("Interfaz de Inserción de Datos")
ventana.geometry('300x300')  # Establecer el tamaño de la ventana

# Cargar el estilo de Plastik
style = ThemedStyle(ventana)
style.set_theme("plastik")

# Etiquetas y campos de entrada
label_nombre = ttk.Label(ventana, text="Nombre:")
label_nombre.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
entry_nombre = ttk.Entry(ventana)
entry_nombre.grid(row=0, column=1, padx=10, pady=5)

label_password = ttk.Label(ventana, text="Contraseña:")
label_password.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
entry_password = ttk.Entry(ventana, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=5)

# Botón de inserción
btn_insertar = ttk.Button(ventana, text="Insertar Datos", command=insertar_datos)
btn_insertar.grid(row=2, columnspan=2, padx=10, pady=10)

# Centrar ventana
center_window(ventana)

# Ejecutar ventana
ventana.mainloop()
