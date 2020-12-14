from flask_restful import Resource
from flask import request
from Blog_models import BlogPost, Author
from schemas import BlogPostSchemaRead, BlogPostSchemaWrite
from marshmallow.exceptions import ValidationError
import json


class PostResource(Resource):

    def get(self, author=None, tag=None, id=None):
        if author:
            posts = BlogPost.objects(author=author)
            for p in posts:
                p.modify(inc__post_view=1)
            return json.loads(posts.to_json())
        if tag:
            posts = BlogPost.objects(tags=tag)
            for p in posts:
                p.modify(inc__post_view=1)
            return json.loads(posts.to_json())
        if id:
            posts = BlogPost.objects(id=id)
            posts.modify(inc__post_view=1)
            return json.loads(posts.to_json())
        else:
            posts = BlogPost.objects()
            return json.loads(posts.to_json())

    def post(self):
        try:
            BlogPostSchemaWrite().load(request.json)
        except ValidationError as e:
            return {'text': str(e)}
        post_ = BlogPost(**request.json).save()
        # post_.reload()
        return BlogPostSchemaRead().dump(post_)

    def put(self, id):
        post = BlogPost.objects(id=id)
        post.update(**request.json)
        post.reload()
        return json.loads(post.to_json())

    def delete(self, id):
        post = BlogPost.objects(id=id)
        post.delete()
        posts = BlogPost.objects()
        return json.loads(posts.to_json())
