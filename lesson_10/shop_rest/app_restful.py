from flask import Flask
from flask_restful import Api
from .resources import ShopResource

app = Flask(__name__)
api = Api(app)


api.add_resource(ShopResource, '/shop', '/shop/categories/<string:category>', '/shop/products/<string:product>',
                 '/shop/product/<string:id>')

