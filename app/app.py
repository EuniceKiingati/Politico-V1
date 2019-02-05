from flask import Flask, jsonify, request
import json


def create_app():
    app = Flask(__name__)
    users = []

    @app.route('/api/v1/users', methods=['POST'])
    def sign_up():
        data = request.get_json()
        username = data['username']
        new_user = {}
        new_user['user_id'] = len(users) + 1
        new_user["username"] = username
        new_user["email"] = data['email']
        new_user["password"] = data['password']
        users.append(new_user)

        response = jsonify({
            "message": "user created successfully",
            "status": 201,
            "data": users
        })
        response.status_code = 201
        return response
    return app
