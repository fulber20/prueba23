from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import pandas as pd
import io
import base64
import matplotlib.pyplot as plt
import seaborn as sns

app = Flask(__name__)

# Conexión a la base de datos
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='your_username',
        password='your_password',
        database='ecommerce'
    )

# Convertir la imagen a base64
def convert_image_to_base64(image_blob):
    if image_blob:
        return base64.b64encode(image_blob).decode('utf-8')
    return None

@app.route('/')
def index():
    conn = get_db_connection()

    # Obtener productos disponibles
    products_query = "SELECT * FROM products"
    products_df = pd.read_sql(products_query, conn)
    products = products_df.to_dict(orient='records')
    
    # Convertir imágenes a base64
    for product in products:
        if product.get('image'):
            product['image'] = convert_image_to_base64(product['image'])

    # Obtener productos recomendados basados en ventas
    recommended_query = """
    SELECT p.id, p.name, p.description, p.price, p.image
    FROM products p
    JOIN sales s ON p.id = s.product_id
    GROUP BY p.id
    ORDER BY SUM(s.quantity) DESC
    LIMIT 5
    """
    recommended_df = pd.read_sql(recommended_query, conn)
    recommended_products = recommended_df.to_dict(orient='records')
    
    # Convertir imágenes recomendadas a base64
    for product in recommended_products:
        if product.get('image'):
            product['image'] = convert_image_to_base64(product['image'])
    
    conn.close()
    return render_template('index.html', products=products, recommended_products=recommended_products)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    conn = get_db_connection()
    search_query = """
    SELECT * FROM products WHERE name LIKE %s OR description LIKE %s
    """
    df = pd.read_sql(search_query, conn, params=(f'%{query}%', f'%{query}%'))
    conn.close()

    # Convertir imágenes a base64
    products = df.to_dict(orient='records')
    for product in products:
        if product.get('image'):
            product['image'] = convert_image_to_base64(product['image'])
    
    return render_template('index.html', products=products)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    product_id = request.form['product_id']
    # Lógica para agregar el producto al carrito
    return redirect(url_for('index'))

@app.route('/buy_now', methods=['POST'])
def buy_now():
    product_id = request.form['product_id']
    # Lógica para comprar el producto
    return redirect(url_for('index'))

@app.route('/cart')
def cart():
    # Lógica para mostrar el carrito de compras
    return render_template('cart.html')

@app.route('/recommendations')
def recommendations():
    conn = get_db_connection()
    query = """
    SELECT p.name, SUM(s.quantity) AS total_quantity
    FROM sales s
    JOIN products p ON s.product_id = p.id
    GROUP BY p.name
    """
    df = pd.read_sql(query, conn)
    conn.close()

    # Generar gráfico de barras
    plt.figure(figsize=(10, 6))
    sns.barplot(x='name', y='total_quantity', data=df, palette='viridis')
    plt.title('Cantidad Total Vendida por Producto')
    plt.xlabel('Producto')
    plt.ylabel('Cantidad Vendida')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Guardar gráfico en un buffer y convertir a base64
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    img_base64 = base64.b64encode(img.getvalue()).decode()

    return render_template('recommendations.html', plot_url=img_base64)

if __name__ == '__main__':
    app.run(debug=True)
