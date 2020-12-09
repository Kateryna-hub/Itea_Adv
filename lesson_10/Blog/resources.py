from flask_restful import Resource
from flask import request
from Blog_models import BlogPost, Author
from schemas import BlogPostSchemaRead, BlogPostSchemaWrite
from marshmallow.exceptions import ValidationError
import json


class PostResource(Resource):

    def get(self, author=None, tag=None):
        if author:
            posts = BlogPost.objects(author=author)
            posts.update(inc__post_view=1)
            return json.loads(posts.to_json())
        if tag:
            posts = BlogPost.objects(tags=tag)
            posts.update(inc__post_view=1)
            return json.loads(posts.to_json())

        else:
            posts = BlogPost.objects()
            posts.update(inc__post_view=1)
            return json.loads(posts.to_json())

    def post(self):

        try:
            BlogPostSchemaWrite().load(request.json)
        except ValidationError as e:
            return {'text': str(e)}
        post_ = BlogPost(**request.json).save()
        post_.reload()
        return BlogPostSchemaRead().dump(post_)

    def put(self):
        pass

    def delete(self):
        pass