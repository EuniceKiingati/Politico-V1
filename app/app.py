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

    @app.route('/api/v1/users/login', methods=['POST'])
    def login():
        data = request.get_json()  # getting a json object from request
        username = data['username']  # gets the value that the key represents
        password = data['password']
        for user in users:
            if user['username'] == username and user['password'] == password:  # to loo
                response = jsonify({
                    "message": "User login successful",
                    "status": 200,
                    "data": user
                })
                response.status_code = 200
                return response
        response = jsonify({
            "message": "User login failed, Check your credentials",
            "status": 404,  # not  found
        })
        response.status_code = 404
        return response

    return app
