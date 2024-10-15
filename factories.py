from faker import Faker
from models import Product, db

fake = Faker()

def create_product(name=None, description=None, price=None, category=None, stock=None):
    """
    Factory untuk membuat produk baru.
    Jika argumen tidak diberikan, gunakan faker untuk membuat data acak.
    """
    product = Product(
        name=name or fake.company() + ' ' + fake.word(),
        description=description or fake.text(max_nb_chars=200),
        price=price or round(fake.random_number(digits=5), 2),
        category=category or fake.word(),
        stock=stock or fake.random_int(min=1, max=100)
    )
    db.session.add(product)
    db.session.commit()
    return product

def create_sample_products():
    """
    Membuat beberapa produk sample untuk testing
    """
    # Buat produk spesifik
    create_product(name="Laptop Lenovo", description="Laptop Lenovo terbaru dengan prosesor Intel Core i7", price=1200.00, category="Laptop", stock=20)
    create_product(name="iPhone 14 Pro", description="iPhone 14 Pro dengan layar OLED dan chipset terbaru", price=999.99, category="Smartphone", stock=50)
    create_product(name="Samsung Galaxy S22", description="Smartphone flagship dari Samsung dengan kamera 108MP", price=850.75, category="Smartphone", stock=30)
    create_product(name="MacBook Pro", description="MacBook Pro dengan M2 Chip", price=2000.00, category="Laptop", stock=15)
    create_product(name="Sony WH-1000XM5", description="Headphone noise cancelling terbaru dari Sony", price=350.00, category="Accessories", stock=40)

    # Buat beberapa produk acak
    for _ in range(1000000):
        create_product()

    print("Sample products created!")

