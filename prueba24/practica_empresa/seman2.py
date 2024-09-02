#importar librerias
import pandas as pd
import numpy as np
from sklearn.linear_model 
import LinearRegression
from sklearn.model_selection 
import train_test_split
from sklearn.metrics 
import mean_squared_error

# Datos de ejemplo
data = {
    'horas': [200, 145, 204, 300, 270, 304, 25, 35],
    'participantes': [10, 20, 15, 20, 25, 8, 18, 22],
    'complejidad': [1, 2, 3, 5, 8, 9, 10, 5],
    'costo': [95, 140, 250, 195, 80, 95, 100, 150]  # Costos en dólares
}

# Convertir el diccionario a un DataFrame
df = pd.DataFrame(data)

# Definir características (X) y variable objetivo (y)
X = df[['horas', 'participantes', 'complejidad']]
y = df['costo']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo
model = LinearRegression()
model.fit(X_train, y_train)

# Hacer predicciones
y_pred = model.predict(X_test)

# Evaluar el modelo
mse = mean_squared_error(y_test, y_pred)
print(f'Error Cuadrático Medio (MSE): {mse:.2f}')

# Ejemplo de predicción: Estimar el costo para un programa de 60 horas, 30 participantes y complejidad alta (3)
new_data = np.array([[60, 30, 3]])
predicted_cost = model.predict(new_data)
print(f'Predicción del costo para un programa de capacitación de 60 horas, 30 participantes y complejidad alta: S/.{predicted_cost[0]:,.2f}')
