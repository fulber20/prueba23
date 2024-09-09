import pandas as pd
import mysql.connector  # O el conector que estés utilizando (sqlite3, psycopg2, etc.)

# Función para obtener una conexión a la base de datos
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='ecommerce'
    )

# Leer datos desde una base de datos SQL y guardarlos como un archivo CSV
def export_data_to_csv():
    conn = get_db_connection()
    query = "SELECT * FROM products"  # Cambia 'your_table_name' por el nombre de la tabla que quieres leer
    datos = pd.read_sql(query, conn)
    
    # Guardar el DataFrame como un archivo CSV
    datos.to_csv('C:/Users/FULBER/Documents/lavadero/name.csv', index=False)
    
    # Imprimir las primeras filas del DataFrame
    print(datos.head())
    
    conn.close()

# Ejecutar la función
export_data_to_csv()
