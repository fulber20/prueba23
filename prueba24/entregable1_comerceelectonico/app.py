from flask import Flask, render_template, request, redirect, url_for, flash, session
from functools import wraps
import mysql.connector
import pandas as pd
import io
import base64
import matplotlib.pyplot as plt
import seaborn as sns

app = Flask(__name__)
app.secret_key = 'your_secret_key'  
USERS = {
    'administrador': 'ponce123'  }

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='your_username',
        password='your_password',
        database='ecommerce'
    )

def convert_image_to_base64(image_blob):
    if image_blob:
        return base64.b64encode(image_blob).decode('utf-8')
    return None

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Entregable 1: Manipulación y Análisis de Datos

@app.route('/')
def index():
    conn = get_db_connection()

    products_query = "SELECT * FROM products"
    products_df = pd.read_sql(products_query, conn)
    products = products_df.to_dict(orient='records')
    
    for product in products:
        if product.get('image'):
            product['image'] = convert_image_to_base64(product['image'])


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

    products = df.to_dict(orient='records')
    for product in products:
        if product.get('image'):
            product['image'] = convert_image_to_base64(product['image'])
    
    return render_template('index.html', products=products)

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

    plt.figure(figsize=(10, 6))
    sns.barplot(x='name', y='total_quantity', data=df, palette='viridis')
    plt.title('Cantidad Total Vendida por Producto')
    plt.xlabel('Producto')
    plt.ylabel('Cantidad Vendida')
    plt.xticks(rotation=45)
    plt.tight_layout()

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    img_base64 = base64.b64encode(img.getvalue()).decode()

    return render_template('recommendations.html', plot_url=img_base64)

@app.route('/upload_csv', methods=['GET', 'POST'])
@login_required
def upload_csv():
    if request.method == 'POST':
        file = request.files.get('file')
        if file and file.filename.endswith('.csv'):
            df = pd.read_csv(file)
            conn = get_db_connection()
            cursor = conn.cursor()

            for index, row in df.iterrows():
                cursor.execute("""
                INSERT INTO products (name, description, price, image)
                VALUES (%s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                description = VALUES(description),
                price = VALUES(price),
                image = VALUES(image)
                """, (row['name'], row['description'], row['price'], row.get('image')))
            conn.commit()
            conn.close()
            
            flash('Archivo CSV procesado exitosamente')
            return redirect(url_for('admin'))
        else:
            flash('Por favor, sube un archivo CSV válido')
    
    return render_template('upload_csv.html')

# Entregable 2: Sistema de Recomendación y Administración

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if USERS.get(username) == password:
            session['username'] = username
            return redirect(url_for('admin'))
        else:
            flash('Credenciales incorrectas')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/admin')
@login_required
def admin():
    conn = get_db_connection()
    recommended_query = """
    SELECT p.id, p.name, p.description, p.price, SUM(s.quantity) AS total_quantity
    FROM products p
    JOIN sales s ON p.id = s.product_id
    GROUP BY p.id
    ORDER BY SUM(s.quantity) DESC
    LIMIT 5
    """
    recommended_df = pd.read_sql(recommended_query, conn)
    recommended_products = recommended_df.to_dict(orient='records')


    all_products_query = "SELECT * FROM products"
    all_products_df = pd.read_sql(all_products_query, conn)
    all_products = all_products_df.to_dict(orient='records')
    
    conn.close()
    return render_template('admin.html', recommended_products=recommended_products, all_products=all_products)

@app.route('/add_product', methods=['POST'])
@login_required
def add_product():
    name = request.form['name']
    description = request.form['description']
    price = request.form['price']

    image = request.files.get('image')
    image_blob = None
    if image and image.filename:
        image_blob = image.read()

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, description, price, image) VALUES (%s, %s, %s, %s)", (name, description, price, image_blob))
    conn.commit()
    conn.close()
    
    flash('Producto agregado exitosamente')
    return redirect(url_for('admin'))

@app.route('/delete_product', methods=['POST'])
@login_required
def delete_product():
    product_id = request.form['product_id']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id = %s", (product_id,))
    conn.commit()
    conn.close()
    
    flash('Producto eliminado exitosamente')
    return redirect(url_for('admin'))

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    product_id = request.form['product_id']
    
    return redirect(url_for('index'))

@app.route('/buy_now', methods=['POST'])
def buy_now():
    product_id = request.form['product_id']

    return redirect(url_for('index'))

@app.route('/cart')
def cart():

    return render_template('cart.html')

if __name__ == '__main__':
    app.run(debug=True)
