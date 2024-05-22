import psycopg2
from Conexion import conectar_bd

def ver_inventario():
    try:
        conexion = conectar_bd()
        if conexion is not None:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM Productos")
            resultados = cursor.fetchall()
            conexion.close()
            return resultados
    except psycopg2.Error as error:
        print("Error al conectar a la base de datos:", error)
        return None

def agregar_producto(nombre, descripcion, unidades, fecha_ingreso, id_emp):
    try:
        conexion = conectar_bd()
        if conexion is not None:
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO Productos (Nombre, Descripcion, Unidades, Fecha_Ingreso, Id_Emp) VALUES (%s, %s, %s, %s, %s)", 
                           (nombre, descripcion, unidades, fecha_ingreso, id_emp))
            conexion.commit()
            conexion.close()
            return True
    except psycopg2.Error as error:
        print("Error al agregar producto:", error)
        return False

def eliminar_producto(id_producto):
    try:
        conexion = conectar_bd()
        if conexion is not None:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM Productos WHERE Id_Producto = %s", (id_producto,))
            producto = cursor.fetchone()
            if producto:
                cursor.execute("DELETE FROM Productos WHERE Id_Producto = %s", (id_producto,))
                conexion.commit()
                conexion.close()
                return True
            else:
                return False
    except psycopg2.Error as error:
        print("Error al eliminar producto:", error)
        return False
