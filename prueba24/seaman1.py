import pandas as pd
import numpy as np 
#datos de la empresa
Date = {
    'Curso': [
        'SUPERVISOR DE TRABAJOS DE ALTO RIESGO',
        'TRABAJOS EN CALIENTE',
        'TRABAJOS EN ALTURA',
        'TRABAJOS ELÉCTRICOS',
        'METRADOS EN EDIFICACIONES',
        'ELABORACION DE COSTOS Y PRESUPUESTOS DE OBRA',
        'PROGRAMACIÓN Y CONTROL DE OBRAS'
    ],
    'DNI': [45592328, 45592328, 45592328, 45592328, 45089649, 45089649,  45089649],
    'Nombres ': [
        'NATHALY  CARPIO',
        'NATHALY  CARPIO',
        'NATHALY  CARPIO',
        'NATHALY CARDENAS',
        'JOSE HINOSTROZA',
        'JOSE HINOSTROZA',
        'JOSE EDUARDO'
    ],
    'F. Inicio': ['2023-09-11', '2024-02-07', '2024-03-02', '2024-04-05', '2023-09-05', '2023-10-06', '2023-11-04'],
    'F. Final': ['2024-04-29', '2024-02-28', '2024-03-28', '2024-04-27', '2024-01-31', '2024-02-28', '2024-03-30']
}

df = pd.DataFrame(Date)

# Convertir las columnas de fecha a formato datetime
df['F. Inicio'] = pd.to_datetime(df['F. Inicio'], format='%Y-%m-%d')
df['F. Final'] = pd.to_datetime(df['F. Final'], format='%Y-%m-%d')

print(df)
