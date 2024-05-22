import tkinter as tk
from tkinter import ttk
import os
from Funciones import ver_inventario, agregar_producto, eliminar_producto

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
    def agregar():
        nombre = entry_nombre.get()
        descripcion = entry_descripcion.get()
        unidades = entry_unidades.get()
        fecha_ingreso = entry_fecha_ingreso.get()
        id_emp = entry_id_emp.get()
        if agregar_producto(nombre, descripcion, unidades, fecha_ingreso, id_emp):
            print("Producto agregado correctamente.")
        else:
            print("Error al agregar producto.")
        entry_nombre.delete(0, tk.END)
        entry_descripcion.delete(0, tk.END)
        entry_unidades.delete(0, tk.END)
        entry_fecha_ingreso.delete(0, tk.END)
        entry_id_emp.delete(0, tk.END)

    ventana = tk.Toplevel(ventana_principal)
    ventana.title("Agregar Producto")

    tk.Label(ventana, text="Nombre:").pack()
    entry_nombre = tk.Entry(ventana)
    entry_nombre.pack()

    tk.Label(ventana, text="Descripción:").pack()
    entry_descripcion = tk.Entry(ventana)
    entry_descripcion.pack()

    tk.Label(ventana, text="Unidades:").pack()
    entry_unidades = tk.Entry(ventana)
    entry_unidades.pack()

    tk.Label(ventana, text="Fecha de Ingreso (YYYY-MM-DD):").pack()
    entry_fecha_ingreso = tk.Entry(ventana)
    entry_fecha_ingreso.pack()

    tk.Label(ventana, text="ID del Empleado (opcional):").pack()
    entry_id_emp = tk.Entry(ventana)
    entry_id_emp.pack()

    tk.Button(ventana, text="Agregar", command=agregar).pack()

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
ventana_principal.geometry("800x400")

tk.Button(ventana_principal, text="Ver Inventario", command=mostrar_inventario).pack()
tk.Button(ventana_principal, text="Agregar Producto", command=ventana_agregar_producto).pack()
tk.Button(ventana_principal, text="Eliminar Producto", command=ventana_eliminar_producto).pack()
tk.Button(ventana_principal, text="SALIR", command=salir).pack()

tree_inventario = ttk.Treeview(ventana_principal, columns=("ID", "Nombre", "Descripción", "Unidades", "Fecha_Ingreso"), show="headings")
tree_inventario.heading("ID", text="ID")
tree_inventario.heading("Nombre", text="Nombre")
tree_inventario.heading("Descripción", text="Descripción")
tree_inventario.heading("Unidades", text="Unidades")
tree_inventario.heading("Fecha_Ingreso", text="Fecha de Ingreso")

tree_inventario.column("ID", width=50)
tree_inventario.column("Nombre", width=100)
tree_inventario.column("Descripción", width=150)
tree_inventario.column("Unidades", width=70)
tree_inventario.column("Fecha_Ingreso", width=200)

tree_inventario.pack()

ventana_principal.mainloop()