import pandas as pd
from sqlalchemy import create_engine

# Crear el motor de conexión utilizando SQLAlchemy
engine = create_engine('mysql+pymysql://root:@localhost/tienda_comercio')

# Leer datos de la base de datos
query = "SELECT * FROM historial_ventas"
df = pd.read_sql(query, engine)

# Exportar a CSV
df.to_csv('historial_ventas.csv', index=False)

