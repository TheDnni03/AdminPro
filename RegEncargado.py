import tkinter as tk
import os
import psycopg2
from Conexion import conectar_bd  # Importar la función conectar_bd desde el módulo Conexion.py

def verificar_usuario():
    # Obtener los datos ingresados por el usuario
    nombre = entry_nombre.get()
    contraseña = entry_contraseña.get()
    # Conectar a la base de datos utilizando la función importada
    conexion = conectar_bd()
    if conexion:
        try:
            cursor = conexion.cursor()
            # Consulta para verificar el usuario en la base de datos
            cursor.execute("SELECT * FROM Usuario WHERE Usuario = %s AND Password = %s", (nombre, contraseña))
            resultado = cursor.fetchone()  # Obtener el primer resultado
            if resultado:
                label_resultado.config(text="Usuario encontrado en la base de datos.")
                # Cerrar la ventana actual
                ventana.destroy()
                # Abrir la ventana del empleado
                os.system("python VentanaEncargado.py")
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
ventana.geometry("500x200")  # Establecer las dimensiones de la ventana

# Etiqueta y campo de entrada para el nombre
label_nombre = tk.Label(ventana, text="Nombre:")
label_nombre.pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

# Etiqueta y campo de entrada para la contraseña
label_contraseña = tk.Label(ventana, text="Contraseña:")
label_contraseña.pack()
entry_contraseña = tk.Entry(ventana, show="*")  # El texto se muestra como asteriscos para ocultar la contraseña
entry_contraseña.pack()

# Botón para verificar el usuario
boton_verificar = tk.Button(ventana, text="Verificar Usuario", command=verificar_usuario)
boton_verificar.pack()

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(ventana, text="")
label_resultado.pack()

# Ejecutar el bucle de eventos principal
ventana.mainloop()
