from flask import Flask, request, jsonify, Response
from lesson_10.application.models import User

app = Flask(__name__)


@app.route('/user', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/user/<string:user_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def user(user_id=None):
    if  request . method  ==  'GET' :
        users = User.objects()
        users_json = users.to_json()
        return Response(users_json, content_type='application/json')

    elif request.method == 'POST':
        user = User(**request.json).save()
        user_json = user.to_json()
        return Response(user_json, content_type='application/json')

    elif request.method == 'PUT' and user_id:
        user = User.objects().get(id=user_id)
        user.update(**request.json)
        user.reload()
        return Response(user.to_json(), content_type='application/json')

    elif request.method == 'DELETE' and user_id:
        User.objects(id=user_id).delete()
        return jsonify({'status': 'Deleted'})
    else:
        return jsonify({'status': 'Error'})


app.run(debug=True)
