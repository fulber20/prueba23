import numpy as np
from datetime import datetime

# Datos de entrada
cursos = [
    'SUPERVISOR DE TRABAJOS DE ALTO RIESGO',
    'TRABAJOS EN CALIENTE',
    'TRABAJOS EN ALTURA',
    'TRABAJOS ELÉCTRICOS',
    'METRADOS EN EDIFICACIONES',
    'ELABORACION DE COSTOS Y PRESUPUESTOS DE OBRA',
    'PROGRAMACIÓN Y CONTROL DE OBRAS'
]

f_inicio = ['2023-09-11', '2024-02-07', '2024-03-02', '2024-04-05', '2023-09-05', '2023-10-06', '2023-11-04']
f_final = ['2024-04-29', '2024-02-28', '2024-03-28', '2024-04-27', '2024-01-31', '2024-02-28', '2024-03-30']

# Convertir las fechas a objetos datetime y luego a valores numéricos (días desde una fecha base)
base_date = datetime(1970, 1) 

def date_to_days(date_st):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    return (date_obj - base_date).days

# Convertir las fechas 
f_inicio_dias = np.array([date_to_days(date) for date in f_inicio])
f_final_dias = np.array([date_to_days(date) for date in f_final])

# Calcular la duración 
duraciones_dias = f_final_dias - f_inicio_dias

# Convertir la duración a horas
duraciones_horas = duraciones_dias * 24

# Imprimir el nombre del curso junto con su duración en días y horas
print("Duración de cada curso:")
for curso, duracion_dia, duracion_hora in zi(cursos, duraciones_dias, duraciones_horas):
    print(f"{curso}: {duracion_dia} días ({duracion_hora} horas)")
