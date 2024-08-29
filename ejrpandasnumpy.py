import pandas as pd
base={ 
    'Nombre': ['Juan','Ana','Luis','Marta'],
    'Edad':[15,14,16,15],
    'Nota':[8.5,9.0,7.5,8.0]
}
base=pd.DataFrame(base)
print(" original")
print(base)

print("actualizado")
base['Ciudad'] = ['Lima','Huánuco','Hucallali','Tingo']

print(base)

