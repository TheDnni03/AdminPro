import tkinter as tk
import os
import psycopg2
from Conexion import conectar_bd

def ver_inventario():
    try:
        # Conectar a la base de datos
        conexion = conectar_bd()
        if conexion is not None:
            cursor = conexion.cursor()
        
            # Consulta para seleccionar todos los registros de la tabla "Usuarios"
            cursor.execute("SELECT * FROM Usuarios")
        
            # Obtener todos los resultados
            resultados = cursor.fetchall()
        
            # Mostrar los resultados en el widget de texto
            texto_inventario.delete("1.0", tk.END)  # Limpiar el contenido anterior
            for resultado in resultados:
                texto_inventario.insert(tk.END, str(resultado) + "\n")
        
            conexion.close()
    except psycopg2.Error as error:
        print("Error al conectar a la base de datos:", error)

def agregar_producto():
    # Función para agregar un nuevo usuario a la base de datos
    def agregar_usuario():
        nombre = entry_nombre.get()
        password = entry_password.get()
        try:
            conexion = conectar_bd()
            if conexion is not None:
                cursor = conexion.cursor()
                cursor.execute("INSERT INTO Usuarios (nombre, password) VALUES (%s, %s)", (nombre, password))
                conexion.commit()
                print("Usuario agregado correctamente.")
                conexion.close()
        except psycopg2.Error as error:
            print("Error al agregar usuario:", error)
        
        # Limpiar los campos de entrada después de agregar el usuario
        entry_nombre.delete(0, tk.END)
        entry_password.delete(0, tk.END)

    # Crear una nueva ventana para agregar usuario
    ventana_agregar_usuario = tk.Toplevel(ventana)
    ventana_agregar_usuario.title("Agregar Usuario")

    # Etiqueta y campo de entrada para el nombre
    label_nombre = tk.Label(ventana_agregar_usuario, text="Nombre:")
    label_nombre.pack()
    entry_nombre = tk.Entry(ventana_agregar_usuario)
    entry_nombre.pack()

    # Etiqueta y campo de entrada para la contraseña
    label_password = tk.Label(ventana_agregar_usuario, text="Contraseña:")
    label_password.pack()
    entry_password = tk.Entry(ventana_agregar_usuario, show="*")
    entry_password.pack()

    # Botón para agregar el usuario
    boton_agregar_usuario = tk.Button(ventana_agregar_usuario, text="Agregar", command=agregar_usuario)
    boton_agregar_usuario.pack()

def eliminar_producto():
    # Función para eliminar un usuario de la base de datos
    def eliminar_usuario():
        nombre = entry_nombre.get()
        try:
            conexion = conectar_bd()
            if conexion is not None:
                cursor = conexion.cursor()
                
                # Verificar si el usuario existe
                cursor.execute("SELECT * FROM Usuarios WHERE nombre = %s", (nombre,))
                usuario = cursor.fetchone()
                
                if usuario:
                    # Si el usuario existe, proceder con la eliminación
                    cursor.execute("DELETE FROM Usuarios WHERE nombre = %s", (nombre,))
                    conexion.commit()
                    print("Usuario eliminado correctamente.")
                    
                    # Mostrar mensaje en la ventana principal
                    mensaje_confirmacion = tk.Label(ventana, text=f"Usuario '{nombre}' eliminado correctamente.")
                    mensaje_confirmacion.pack()
                    
                    # Cerrar la ventana secundaria después de 5 segundos
                    ventana_eliminar_usuario.after(5000, ventana_eliminar_usuario.destroy)
                else:
                    print("El usuario no existe.")
                    # Mostrar mensaje de error en la ventana secundaria
                    mensaje_error = tk.Label(ventana_eliminar_usuario, text=f"El usuario '{nombre}' no existe.")
                    mensaje_error.pack()
                    
        except psycopg2.Error as error:
            print("Error al eliminar usuario:", error)
        
        # Limpiar el campo de entrada después de eliminar el usuario
        entry_nombre.delete(0, tk.END)

    # Crear una nueva ventana para eliminar usuario
    ventana_eliminar_usuario = tk.Toplevel(ventana)
    ventana_eliminar_usuario.title("Eliminar Usuario")

    # Etiqueta y campo de entrada para el nombre
    label_nombre = tk.Label(ventana_eliminar_usuario, text="Nombre del usuario a eliminar:")
    label_nombre.pack()
    entry_nombre = tk.Entry(ventana_eliminar_usuario)
    entry_nombre.pack()

    # Botón para eliminar el usuario
    boton_eliminar_usuario = tk.Button(ventana_eliminar_usuario, text="Eliminar", command=eliminar_usuario)
    boton_eliminar_usuario.pack()

def salir():
    # Cerrar la ventana actual
    ventana.destroy()
    # Ejecutar el archivo Index.py
    os.system("python Index.py")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Interfaz gráfica")
ventana.geometry("500x300")

# Botón para ver el inventario
boton_ver_inventario = tk.Button(ventana, text="Ver Inventario", command=ver_inventario)
boton_ver_inventario.pack()

# Botón para agregar un producto
boton_agregar_producto = tk.Button(ventana, text="Agregar Producto", command=agregar_producto)
boton_agregar_producto.pack()

# Botón para eliminar un producto
boton_eliminar_producto = tk.Button(ventana, text="Eliminar Producto", command=eliminar_producto)
boton_eliminar_producto.pack()

# Botón para salir de la aplicación
boton_salir = tk.Button(ventana, text="SALIR", command=salir)
boton_salir.pack()

# Widget de texto para mostrar el inventario
texto_inventario = tk.Text(ventana, height=10, width=50)
texto_inventario.pack()

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
