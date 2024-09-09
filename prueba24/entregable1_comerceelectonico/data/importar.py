import pandas as pd
from sqlalchemy import create_engine

# Leer datos de la base de datos
query = "SELECT * FROM sales"
df = pd.read_sql(query, engine)

# Exportar a CSV
df.to_csv('sales.csv', index=False)

