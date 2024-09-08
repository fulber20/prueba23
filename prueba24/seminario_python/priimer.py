import pandas as pd

# Usar pd.read_excel para leer un archivo Excel
datos = pd.read_excel('C:/Users/FULBER/Documents/lavadero/producto.xlsx', header=None)

# Guardar el DataFrame como un archivo CSV
datos.to_csv('C:/Users/FULBER/Documents/lavadero/producto.csv', index=False)

# Imprimir las primeras filas del DataFrame
print(datos.head())
