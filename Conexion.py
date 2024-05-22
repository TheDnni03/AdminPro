import psycopg2

def conectar_bd():
    try:
        conexion = psycopg2.connect(
            dbname="Almacen",
            user="postgres",
            password="D11Z08V03",
            host="localhost",
            port="5432"
        )
        return conexion
    except psycopg2.Error as e:
        print("Error al conectar a la base de datos:", e)
        return None