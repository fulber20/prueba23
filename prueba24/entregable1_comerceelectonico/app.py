from flask import Flask, request, jsonify, render_template
import pandas as pd

app = Flask(__name__)

# Cargar datos
ventas = pd.read_csv('historial_ventas.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommendations', methods=['GET'])
def get_recommendations():
    user_id = request.args.get('user-id')
    # Ejemplo simple de recomendación
    recommendations = {
        "user_id": user_id,
        "recommended_products": ["Producto A", "Producto B", "Producto C"]
    }
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
