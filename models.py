from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=True)
    stock = db.Column(db.Integer, nullable=False)

# Serializer untuk Product
class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    description = fields.Str()
    price = fields.Float()
    category = fields.Str()
    stock = fields.Int()

# Instance untuk serialisasi
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
