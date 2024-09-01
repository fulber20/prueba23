#operaciones con numpy y pandas con los datos emmp
import pandas as pd
import numpy as np


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
        "SUPERVISOR DE TRABAJOS DE ALTO RIESGO", "TRABAJOS EN CALIENTE", "TRABAJOS EN ALTURA", 
        "TRABAJOS ELÉCTRICOS", "METRADOS EN EDIFICACIONES", "ELABORACION DE COSTOS Y PRESUPUESTOS DE OBRA", 
        "PROGRAMACIÓN Y CONTROL DE OBRAS", "VALORIZACION Y LIQUIDACION DE OBRAS PÚBLICAS", 
        "Seguridad, Salud Ocupacional y Medio Ambiente en Minería y Construcción", 
        "GESTIÓN DE INVERSIÓN PÚBLICA INVIERTE.PE", "SUPERVISOR SSOMA", "GESTIÓN AMBIENTAL", 
        "METRADOS EN EDIFICACIONES", "ELABORACION DE COSTOS Y PRESUPUESTOS DE OBRA", 
        "PROGRAMACIÓN Y CONTROL DE OBRAS", "VALORIZACION Y LIQUIDACION DE OBRAS PÚBLICAS", 
        "Seguridad, Salud Ocupacional y Medio Ambiente en Minería y Construcción", 
        "METRADOS EN EDIFICACIONES", "Seguridad, Salud Ocupacional y Medio Ambiente en Minería y Construcción", 
        "SUPERVISOR DE TRABAJOS DE ALTO RIESGO", "TRABAJOS EN CALIENTE", "TRABAJOS EN ALTURA", 
        "TRABAJOS CON IZAJE DE CARGA", "METRADOS EN EDIFICACIONES", "ELABORACION DE COSTOS Y PRESUPUESTOS DE OBRA", 
        "PROGRAMACIÓN Y CONTROL DE OBRAS", "VALORIZACION Y LIQUIDACION DE OBRAS PÚBLICAS", 
        "MODELADO BIM REVIT ESTRUCTURAS", "METRADOS EN EDIFICACIONES", "ELABORACION DE COSTOS Y PRESUPUESTOS DE OBRA"
    ],
    "DNI": [
        "45592022", "45592022", "45592022", "45592022", "45099189", "45099189", 
        "45099189", "45099189", "72230861", "41789538", "44093903", "44093903", 
        "43108216", "43108216", "43108216", "43108216", "46793173", "71028470", 
        "70893310", "77320378", "77320378", "77320378", "77320378", "42447315", 
        "42447315", "42447315", "42447315", "42447315", "76025711", "76025711"
    ],
    "Nombres_Apellidos": [
        "NATHALY MILAGROS CARDENAS CARPIO", "NATHALY MILAGROS CARDENAS CARPIO", 
        "NATHALY MILAGROS CARDENAS CARPIO", "NATHALY MILAGROS CARDENAS CARPIO", 
        "JOSE EDUARDO HINOSTROZA ARAUJO", "JOSE EDUARDO HINOSTROZA ARAUJO", 
        "JOSE EDUARDO HINOSTROZA ARAUJO", "JOSE EDUARDO HINOSTROZA ARAUJO", 
        "ZEGARRA QUIÑONES MARIA CRISTINA", "CESAR RICARDO ROSADO ROLDAN", 
        "OSCAR RAMOS PALLI", "OSCAR RAMOS PALLI", "WASHINGTON MACEDO CHALLCO", 
        "WASHINGTON MACEDO CHALLCO", "WASHINGTON MACEDO CHALLCO", 
        "WASHINGTON MACEDO CHALLCO", "GABRIEL NELSON ARAGON VILCAS", 
        "ADRIANA JAZMIN MIRANDA MARTINEZ", "JORGE LUIS TUYA ZAMBRANO", 
        "FREDY CONOVILCA OSORES", "FREDY CONOVILCA OSORES", "FREDY CONOVILCA OSORES", 
        "FREDY CONOVILCA OSORES", "ING. EDSON HERIBERTO QUISPE ROJAS", 
        "ING. EDSON HERIBERTO QUISPE ROJAS", "ING. EDSON HERIBERTO QUISPE ROJAS", 
        "ING. EDSON HERIBERTO QUISPE ROJAS", "ING. EDSON HERIBERTO QUISPE ROJAS", 
        "ALANYA CAMARENA CLIDER YOVANY", "ALANYA CAMARENA CLIDER YOVANY"
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


df['F. Inicio'] = pd.to_datetime(df['F. Inicio'], dayfirst=True)
df['F. Final'] = pd.to_datetime(df['F. Final'], dayfirst=True)

# Calcular la duración de cada curso en días y horas
df['Duración (días)'] = (df['F. Final'] - df['F. Inicio']).dt.dys
df['Duración (horas)'] = df['Duración (días)'] * 24


total_clientes = df['DNI'].nuniqgroupby()


cursos_por_cliente = df.groupby('Nombres_Apellidos').size().resest(name='Número de Cursos')


print(f"Cantidad total de clientes: {total_clientes}")
print("\nNúmero de cursos por cliente:")
print(cursos_por_cliente)

print("\nDuración de cada curso en días y horas:")
print(df[['Código', 'Curso', 'Nombres_Apellidos', 'Duración (días)', 'Duración (horas)']])
