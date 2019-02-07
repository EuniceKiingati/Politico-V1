import re
from flask import jsonify, abort
from app.api.v1.models import users


def bad_request(message):
    response = jsonify({
        "error": message,
        "status": 400,
    })
    response.status_code = 400
    abort(response)


class UserValidation():
    def __init__(self, data):
        self.data = data

    def validate_signup(self):
        if not self.data:
            message = "You must provide signup data"
            return bad_request(message)

        username = self.data['username']
        if username == "":
            message = 'Username is missing'
            return bad_request(message)
        for user in users:
            if username == user["username"]:
                message = "username {} already taken".format(username)
                return bad_request(message)
        if type(username) != str:
            message = "Username must be a string"
            return bad_request(message)
        password = self.data['password']
        if password == "":
            message = "Password is missing"
            return bad_request(message)
        if type(password) != str:
            message = "Password must be a string"
            return bad_request(message)
        if len(password) <= 6 or len(password) > 12:
            message = "Password must be at least 6 and at most 10 ch long"
            return bad_request(message)
        elif not any(char.isdigit() for char in password):
            message = "Password must have a digit"
            return bad_request(message)
        elif not any(char.isupper() for char in password):
            message = "Password must have an upper case character"
            return bad_request(message)
        elif not any(char.islower() for char in password):
            message = "Password must have a lower case character"
            return bad_request(message)
        elif not re.search("[#@$]", password):
            message = "Password must have one of the special charater [#@$]"
            return bad_request(message)
        return True

    def validate_login(self):
        if not self.data:

            message = "You must provide login data"
            return bad_request(message)

        # gets the value that the key represents
        username = self.data['username']
        if username == "":
            message = 'Username is missing'
            return bad_request(message)
        password = self.data['password']
        if password == "":
            message = "Password is missing"
            return bad_request(message)
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
            "status": 401,  # not  found
        })
        response.status_code = 401
        return response