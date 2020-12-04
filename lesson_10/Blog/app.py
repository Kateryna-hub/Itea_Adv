from flask import Flask, request

app = Flask(__name__)


@app.route('/post', methods=['GET', 'PAST', 'PUT', 'DELETE'])
@app.route('/post/<int:post_id>', methods=['GET', 'PAST', 'PUT', 'DELETE'])
def post(post_id=None):
    if request.method == 'GET':
        pass

    if request.method == 'PAST':
        pass

    if request.method == 'PUT':
        pass

    if request.method == 'DELETE':
        pass