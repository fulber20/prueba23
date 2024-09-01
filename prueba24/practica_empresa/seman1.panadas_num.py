import pandas as pd

# Datos originales con nombres ficticios
data = {
    "Código": [
        "R4954-45592022", "R4955-45592022", "R4956-45592022", "R4957-45592022", 
        "R4958-45099189", "R4959-45099189", "R4960-45099189", "R4961-45099189", 
        "R4962-72230861", "R4963-41789538", "R4964-44093903", "R4965-44093903", 
        "R4966-43108216", "R4967-43108216", "R4968-43108216", "R4969-43108216", 
        "R4970-46793173", "R4971-71028470", "R4972-70893310", "R4973-77320378", 
        "R4974-77320378", "R4975-77320378", "R4976-77320378", "R4977-42447315", 
        "R4978-42447315", "R4979-42447315", "R4980-42447315", "R4981-42447315", 
        "R4982-76025711", "R4983-76025711"
    ],
    "Curso": [
        "SUPERVISOR DE TRABAJOS DE ALTO RIESGO", "TRABAJOS EN CALIENTE", "TRABAJOS EN ALTURA", "TRABAJOS ELÉCTRICOS", 
        "METRADOS EN EDIFICACIONES", "ELABORACION DE COSTOS Y PRESUPUESTOS DE OBRA", "PROGRAMACIÓN Y CONTROL DE OBRAS", 
        "VALORIZACION Y LIQUIDACION DE OBRAS PÚBLICAS", "Seguridad, Salud Ocupacional y Medio Ambiente en Minería y Construcción", 
        "GESTIÓN DE INVERSIÓN PÚBLICA INVIERTE.PE", "SUPERVISOR SSOMA", "GESTIÓN AMBIENTAL", "METRADOS EN EDIFICACIONES", 
        "ELABORACION DE COSTOS Y PRESUPUESTOS DE OBRA", "PROGRAMACIÓN Y CONTROL DE OBRAS", "VALORIZACION Y LIQUIDACION DE OBRAS PÚBLICAS", 
        "Seguridad, Salud Ocupacional y Medio Ambiente en Minería y Construcción", "METRADOS EN EDIFICACIONES", 
        "Seguridad, Salud Ocupacional y Medio Ambiente en Minería y Construcción", "SUPERVISOR DE TRABAJOS DE ALTO RIESGO", 
        "TRABAJOS EN CALIENTE", "TRABAJOS EN ALTURA", "TRABAJOS CON IZAJE DE CARGA", "METRADOS EN EDIFICACIONES", 
        "ELABORACION DE COSTOS Y PRESUPUESTOS DE OBRA", "PROGRAMACIÓN Y CONTROL DE OBRAS", "VALORIZACION Y LIQUIDACION DE OBRAS PÚBLICAS", 
        "MODELADO BIM REVIT ESTRUCTURAS", "METRADOS EN EDIFICACIONES", "ELABORACION DE COSTOS Y PRESUPUESTOS DE OBRA"
    ],
    "IDNS": [
        "4559202215", "4559202202", "4559202219", "4559202250", "6845099189", 
        "4509918916", "45099189332", "4509918920", "7223086130", "4541789538", 
        "4409390315", "4409390361", "4310821695", "4310821620", "7543108216", 
        "4310821618", "4679317381", "7102847086", "7089331095", "4077320378", 
        "7732037819", "7732037851", "7732037869", "4244731524", "8042447315", 
        "4244731520", "4244731591", "4244731545", "7602571156", "5776025711"
    ],
    "Nombres_Apellidos": [
        "Laura Rodríguez Pérez", "Carlos Martínez Gómez", "Ana Silva Torres", "Pedro López Vargas", 
        "Luis Fernández Álvarez", "Marta Gómez Fernández", "Jorge Ramírez Morales", "Claudia Martínez López", 
        "Sofia Torres Rodríguez", "David González Castro", "Héctor Morales Ruiz", "Beatriz Fernández Díaz", 
        "Ricardo Pérez Jiménez", "Laura Díaz Márquez", "Luis Alejandro Rodríguez", "Camila Gómez Sánchez", 
        "Antonio Ruiz Martínez", "Laura García Martínez", "Jorge Fernández López", "Alejandra Morales Gómez", 
        "Mónica Castillo Ruiz", "Andrés Fernández López", "Ricardo López Vargas", "José Martínez Rodríguez", 
        "Juan Pablo Gómez", "Ana María Vargas", "Valeria Castro Romero", "Camilo Mendoza Martínez", 
        "Gabriela López Sánchez", "Laura Muñoz Castillo"
    ],
    "F. Inicio": [
        "9/11/2023", "7/02/2024", "2/03/2024", "5/04/2024", "5/09/2023", 
        "6/10/2023", "4/11/2023", "1/12/2023", "5/01/2024", "5/01/2024", 
        "5/02/2024", "5/02/2024", "5/09/2023", "6/10/2023", "4/11/2023", 
        "1/12/2023", "5/01/2024", "5/01/2024", "5/01/2024", "9/11/2023", 
        "7/02/2024", "2/03/2024", "5/04/2024", "5/09/2023", "6/10/2023", 
        "4/11/2023", "1/12/2023", "5/01/2024", "5/09/2023", "6/10/2023"
    ],
    "F. Final": [
        "29/04/2024", "28/02/2024", "28/03/2024", "27/04/2024", "31/01/2024", 
        "28/02/2024", "30/03/2024", "26/04/2024", "29/04/2024", "29/04/2024", 
        "14/05/2024", "14/05/2024", "31/01/2024", "28/02/2024", "30/03/2024", 
        "26/04/2024", "29/04/2024", "29/04/2024", "29/04/2024", "29/04/2024", 
        "28/02/2024", "28/03/2024", "27/04/2024", "31/01/2024", "28/02/2024", 
        "30/03/2024", "26/04/2024", "29/04/2024", "31/01/2024", "28/02/2024"
    ]
}

df = pd.DataFrame(data)

# Convertir las columnas de fechas a datetime
df['F. Inicio'] = pd.to_datetime(df['F. Inicio'], dayfirst=True)
df['F. Final'] = pd.to_datetime(df['F. Final'], dayfirst=True)

# Calcular la duración en días y horas
df['Duración (días)'] = (df['F. Final'] - df['F. Inicio']).dt.days
df['Duración (horas)'] = df['Duración (días)'] * 24

# Contar el número total de clientes
total_clientes = df['IDNS'].nunique()

# Contar cuántos cursos ha tomado cada cliente
cursos_por_cliente = df.groupby('Nombres_Apellidos').size().reset_index(name='Número de Cursos')

# Mostrar resultados
print(f"Cantidad total de clientes: {total_clientes}")
print("\nNúmero de cursos por cliente:")
print(cursos_por_cliente)

print("\nDuración de cada curso en días y horas:")
print(df[['Código', 'Curso', 'Nombres_Apellidos', 'Duración (días)', 'Duración (horas)']])
