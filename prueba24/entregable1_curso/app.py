from flask import Flask, request, jsonify
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import numpy as np

app = Flask(__name__)

# Cargar los datos (deberías reemplazar esto con la carga de tus datos reales)
df = pd.read_csv('C:/Users/FULBER/Documents/lavadero/data.csv')  # Asegúrate de que este CSV tenga columnas como 'user_id', 'product_id', 'quantity'

# Función para obtener recomendaciones
def recommend_products(user_id):
    # Filtrar datos del usuario
    user_data = df[df['user_id'] == user_id]
    
    # Aquí deberías agregar la lógica para recomendar productos basados en el comportamiento
    # Un enfoque simple podría ser recomendar los productos más comprados por el usuario
    recommended_products = user_data.groupby('product_id')['quantity'].sum().sort_values(ascending=False).index.tolist()
    
    return recommended_products

@app.route('/recommendations/<int:user_id>', methods=['GET'])
def get_recommendations(user_id):
    recommendations = recommend_products(user_id)
    return jsonify({'recommended_products': recommendations})

if __name__ == '__main__':
    app.run(debug=True)
