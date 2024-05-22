# main.py
import tkinter as tk
import os
import psycopg2
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import ThemedStyle
from Funciones import ver_inventario, agregar_producto, eliminar_producto
from Conexion import conectar_bd  # Asegúrate de tener este módulo para la conexión a la BD

def mostrar_inventario():
    resultados = ver_inventario()
    for item in tree_inventario.get_children():
        tree_inventario.delete(item)
    
    if resultados is not None:
        for resultado in resultados:
            tree_inventario.insert("", tk.END, values=resultado)
    else:
        print("Error al conectar a la base de datos.")

def ventana_agregar_producto():
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

    ventana = tk.Toplevel(ventana_principal)
    ventana.title("Agregar Producto")
    ventana.geometry('300x300')

    style = ThemedStyle(ventana)
    style.set_theme("plastik")

    ttk.Label(ventana, text="Usuario:").grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
    entry_usuario = ttk.Entry(ventana)
    entry_usuario.grid(row=0, column=1, padx=10, pady=5)

    ttk.Label(ventana, text="Nombre:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
    entry_nombre = ttk.Entry(ventana)
    entry_nombre.grid(row=1, column=1, padx=10, pady=5)

    ttk.Label(ventana, text="Apellido Paterno:").grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
    entry_apellido_paterno = ttk.Entry(ventana)
    entry_apellido_paterno.grid(row=2, column=1, padx=10, pady=5)

    ttk.Label(ventana, text="Apellido Materno:").grid(row=3, column=0, padx=10, pady=5, sticky=tk.E)
    entry_apellido_materno = ttk.Entry(ventana)
    entry_apellido_materno.grid(row=3, column=1, padx=10, pady=5)

    ttk.Label(ventana, text="Contraseña:").grid(row=4, column=0, padx=10, pady=5, sticky=tk.E)
    entry_password = ttk.Entry(ventana, show="*")
    entry_password.grid(row=4, column=1, padx=10, pady=5)

    ttk.Button(ventana, text="Insertar Datos", command=insertar_datos).grid(row=5, columnspan=2, padx=10, pady=10)

def ventana_eliminar_producto():
    def eliminar():
        id_producto = entry_id_producto.get()
        if eliminar_producto(id_producto):
            print("Producto eliminado correctamente.")
        else:
            print("El producto no existe o error al eliminar.")
        entry_id_producto.delete(0, tk.END)

    ventana = tk.Toplevel(ventana_principal)
    ventana.title("Eliminar Producto")

    tk.Label(ventana, text="ID del producto a eliminar:").pack()
    entry_id_producto = tk.Entry(ventana)
    entry_id_producto.pack()

    tk.Button(ventana, text="Eliminar", command=eliminar).pack()

def salir():
    ventana_principal.destroy()
    os.system("python Index.py")

ventana_principal = tk.Tk()
ventana_principal.title("Interfaz gráfica")
ventana_principal.geometry("600x400")

tk.Button(ventana_principal, text="Ver Inventario", command=mostrar_inventario).pack()
tk.Button(ventana_principal, text="Nuevo empleado", command=ventana_agregar_producto).pack()
tk.Button(ventana_principal, text="Eliminar Producto", command=ventana_eliminar_producto).pack()
tk.Button(ventana_principal, text="SALIR", command=salir).pack()

# Crear el Treeview para mostrar el inventario
tree_inventario = ttk.Treeview(ventana_principal, columns=("ID", "Nombre", "Descripción", "Unidades", "Fecha_Ingreso"), show="headings")
tree_inventario.heading("ID", text="ID")
tree_inventario.heading("Nombre", text="Nombre")
tree_inventario.heading("Descripción", text="Descripción")
tree_inventario.heading("Unidades", text="Unidades")
tree_inventario.heading("Fecha_Ingreso", text="Fecha de Ingreso")

# Ajustar el tamaño de las columnas
tree_inventario.column("ID", width=50)
tree_inventario.column("Nombre", width=100)
tree_inventario.column("Descripción", width=150)
tree_inventario.column("Unidades", width=70)
tree_inventario.column("Fecha_Ingreso", width=100)

tree_inventario.pack()

ventana_principal.mainloop()