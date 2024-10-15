from flask import Flask

from factories import create_sample_products
from models import db
from routes import product_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'

# Inisialisasi database
db.init_app(app)

# Register blueprint
app.register_blueprint(product_bp)

# Jalankan aplikasi
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        create_sample_products()
    app.run(debug=True)
