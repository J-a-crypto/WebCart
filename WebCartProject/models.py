from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLAlchemy_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(255))
    decription = db.Column(db.Text)
    price = db.Column(db.Numeric(10,2))
    imageURL = db.Column(db.String(255))

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer, db.ForeighnKey('product.id'))
    quantity = db.Column(db.Integer)

    product = db.relationship('Product', backref=db.backref('carts', lazy=True))


    