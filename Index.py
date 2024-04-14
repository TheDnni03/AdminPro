import psycopg2

# Establece la conexión a la base de datos
conn = psycopg2.connect(
    dbname="almacen",
    user="postgres",
    password="D11Z08V03",
    host="localhost",
    port="5432"
)

# Crea un cursor para ejecutar consultas SQL
cur = conn.cursor()

# Ejemplo de consulta SELECT
cur.execute("SELECT * FROM Usuarios;")
rows = cur.fetchall()

print ('Hola')

# Hacer algo con los datos recuperados
for row in rows:
    print(row)


cur.close()
conn.close()
