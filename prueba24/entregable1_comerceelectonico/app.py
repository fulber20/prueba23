from flask import Flask, render_template

app = Flask(__name__)

# Datos de ejemplo
products = [
    {"id": 1, "name": "Camiseta", "price": 20.0, "description": "Camiseta de algodón", "image": "camiseta.jpg"},
    {"id": 2, "name": "Pantalones", "price": 35.0, "description": "Pantalones de mezclilla", "image": "pantalones.jpg"},
    {"id": 3, "name": "Zapatos", "price": 50.0, "description": "Zapatos de cuero", "image": "zapatos.jpg"},
]

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return render_template('product.html', product=product)
    else:
        return "Producto no encontrado", 404

if __name__ == '__main__':
    app.run(debug=True)
