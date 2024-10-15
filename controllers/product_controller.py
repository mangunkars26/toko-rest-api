from flask import jsonify, request
from models import Product, db, product_schema, products_schema

# GET all Products
def get_all_products():
    try:
        products = Product.query.all()  # Mengambil semua produk dari database
        return jsonify({'products': products_schema.dump(products)})  # Mengembalikan dalam format JSON
    except Exception as e:
        return jsonify({'message': str(e)}), 500

# CREATE Product
def create_product():
    data = request.get_json()
    try:
        product = Product(
            name=data['name'],
            description=data.get('description'),
            price=data['price'],
            category=data.get('category'),
            stock=data['stock']
        )
        db.session.add(product)
        db.session.commit()
        return jsonify({'message': 'Product created', 'product': product_schema.dump(product)}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400


# GET Product by ID
def get_product(id):
    try:
        product = Product.query.get(id)
        if product is None:
            return jsonify({'message': 'Product not found'}), 404
        return jsonify({'product': product_schema.dump(product)})
    except Exception as e:
        return jsonify({'message': str(e)}), 500


# UPDATE Product by ID
def update_product(id):
    data = request.get_json()
    try:
        product = Product.query.get(id)
        if product is None:
            return jsonify({'message': 'Product not found'}), 404

        product.name = data.get('name', product.name)
        product.description = data.get('description', product.description)
        product.price = data.get('price', product.price)
        product.category = data.get('category', product.category)
        product.stock = data.get('stock', product.stock)

        db.session.commit()
        return jsonify({'message': 'Product updated', 'product': product_schema.dump(product)})
    except Exception as e:
        return jsonify({'message': str(e)}), 400


# DELETE Product by ID
def delete_product(id):
    try:
        product = Product.query.get(id)
        if product is None:
            return jsonify({'message': 'Product not found'}), 404

        db.session.delete(product)
        db.session.commit()
        return jsonify({'message': 'Product deleted'})
    except Exception as e:
        return jsonify({'message': str(e)}), 500
