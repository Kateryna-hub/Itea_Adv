from flask import Flask
from flask_restful import Api
from .resources import PostResource

app = Flask(__name__)
api = Api(app)


api.add_resource(PostResource, '/shop', '/shop/categories/<string:category>', '/shop/products/<string:product>')

