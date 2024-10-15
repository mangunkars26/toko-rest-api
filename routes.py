from crypt import methods

from flask import Blueprint
from controllers.product_controller import (
    create_product,
    get_product,
    update_product,
    delete_product,
    get_all_products
)

product_bp = Blueprint('product_bp', __name__)

# Rute CRUD untuk Product
product_bp.route('/product', methods=['GET'])(get_all_products)
product_bp.route('/product', methods=['POST'])(create_product)
product_bp.route('/product/<int:id>', methods=['GET'])(get_product)
product_bp.route('/product/<int:id>', methods=['PUT'])(update_product)
product_bp.route('/product/<int:id>', methods=['DELETE'])(delete_product)
