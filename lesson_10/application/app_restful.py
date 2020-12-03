from flask_restful import Api
from flask import request

app = Flask(__name__)
api = Api(app)

api.add_resources(UserResource, '/user')