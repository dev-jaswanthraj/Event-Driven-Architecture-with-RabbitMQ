from flask import Flask, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
from flask_cors import CORS
from flask_migrate import Migrate
import requests
from producer import publish

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///main.db"
CORS(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))

    def get_object(self):
        return {'id': self.id, 'title': self.title, 'image': self.image}
    
class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'product_id', name = 'user_product_unique')


@app.route("/api/products")
def index():
    return jsonify([p.get_object() for p in Product.query.all()])

@app.route('/api/products/<int:id>/like', methods = ['post'])
def like(id):
    req = requests.get("http://127.0.0.1:8000/api/user")
    json = req.json()
    try:
        productuser = ProductUser(user_id = json['id'], product_id = id)
        db.session.add(productuser)
        db.session.commit()

        publish('product_liked', id)
    except:
        abort(400, 'You already liked the image.')
    return jsonify({
        'message': 'Success'
    })