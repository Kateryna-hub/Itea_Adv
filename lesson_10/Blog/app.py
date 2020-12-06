from flask import Flask, request, jsonify, Response
from Blog_models import Post, Author


app = Flask(__name__)


@app.route('/post', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/post/<int:post_id>', methods=['GET', 'PAST', 'PUT', 'DELETE'])
def post(post_id=None):
    if request.method == 'GET':
        posts = Post.objects()
        posts_json = posts.to_json()
        return Response(posts_json, content_type='application/json')

    if request.method == 'POST':
        post = Post(**request.json).save()
        post_json = post.to_json()
        return Response(post_json, content_type='application/json')

    if request.method == 'PUT':
        post = Post.objects().get(id=post_id)
        post.update(**request.json)
        post.reload()
        return Response(post.to_json, content_type='application/json')

    if request.method == 'DELETE':
        pass




app.run(debug=True)
