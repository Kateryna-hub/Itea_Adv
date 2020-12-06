from flask_restful import Resource
from flask import request
from Blog_models import Post, Author
import json


class PostResource(Resource):

    def get(self, id=None):
        if id:
            return json.loads(Post.objects.get(id=id).to_json())

        else:
            posts = Post.objects()
            return json.loads(posts.to_json())

    def post(self):
        post_ = Post(**request.json).save()
        return json.loads(post_.to_json())

    def put(self):
        pass

    def delete(self):
        pass