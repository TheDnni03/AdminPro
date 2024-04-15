import tkinter as tk
import psycopg2

def verificar_usuario():
    # Obtener los datos ingresados por el usuario
    nombre = entry_nombre.get()
    contraseña = entry_contraseña.get()
    # Conectar a la base de datos
    try:
        conexion = psycopg2.connect(
            dbname="almacen",
            user="postgres",
            password="D11Z08V03",
            host="localhost",
            port="5432"
        )
        cursor = conexion.cursor()
        # Consulta para verificar el usuario en la base de datos
        cursor.execute("SELECT * FROM Usuarios WHERE Nombre = %s AND Password = %s", (nombre, contraseña))
        resultado = cursor.fetchone()  # Obtener el primer resultado
        if resultado:
            label_resultado.config(text="Usuario encontrado en la base de datos.")
        else:
            label_resultado.config(text="Usuario no encontrado en la base de datos.")
        conexion.close()
    except psycopg2.Error as error:
        print("Error al conectar a la base de datos:", error)
        label_resultado.config(text="Error al conectar a la base de datos.")

# Crear la ventana
ventana = tk.Tk()
ventana.title("Verificar Usuario")

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
