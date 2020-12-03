from flask_restful import Resource
import json
from flask import request
from .models import User


class UserResources(Resource):

    def get(self, id=None):
        if id:
            return json.loads(User.objects.get(id=id).to_json())

