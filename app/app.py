from flask import Flask, jsonify, request
import json


def create_app():
    app = Flask(__name__)
    users = []
    political_parties = []
    political_offices = []
    

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

    @app.route('/api/v1/parties', methods=['POST', 'GET'])
    def create_party():
        if request.method == 'GET':
            response = jsonify({
                "message": "Pollitical parties retrieved successfully",
                "status": 200,
                "data": political_parties
            })
            response.status_code = 200
            return response
        if request.method == 'POST':
            data = request.get_json()  # getting a json object from request
            party_name = data['party_name']
            hqaddress = data['hqaddress']
            logoUrl = data['logoUrl']
            new_party = {}
            new_party["id"] = len(political_parties) + 1
            new_party["name"] = party_name
            new_party["hqadress"] = hqaddress
            new_party["logoUrl"] = logoUrl
            political_parties.append(new_party)

            response = jsonify({
                "message": "party created successfully",
                "status": 201,
                "data": political_parties
            })
            response.status_code = 201
            return response

    @app.route('/api/v1/parties/<int:party_id>', methods=['GET', 'DELETE'])
    def single_political_party(party_id):
        if request.method == 'DELETE':
            for party in political_parties:
                if party['id'] == party_id:
                    political_parties.remove(party)

                    response = jsonify({
                        "message": "Pollitical parties deleted successfully",
                        "status": 200,
                        "data": political_parties
                    })
                    response.status_code = 200
                    return response
            response = jsonify({
                "message": "invalid id",
                "status": 404,
            })
            response.status_code = 404
            return response
        if request.method == 'GET':
            for party in political_parties:
                if party['id'] == party_id:
                    response = jsonify({
                        "status": 200,
                        "data": party
                    })
                    response.status_code = 200
                    return response
            response = jsonify({
                "message": "invalid id",
                "status": 404,
            })
            response.status_code = 404
            return response

    @app.route('/api/v1/parties/<int:party_id>/name', methods=['PATCH'])
    def edit_party_name(party_id):

        data = request.get_json()  # data being passed
        party_name = data['party_name']
        for party in political_parties:
            if party['id'] == party_id:
                party['name'] = party_name

                response = jsonify({
                    "message": "Pollitical party updated successfully",
                    "status": 200,
                    "data": party
                })
                response.status_code = 200
                return response
        response = jsonify({
            "message": "invalid id",
            "status": 404
        })
        response.status_code = 404
        return response

    @app.route('/api/v1/offices', methods=['GET', 'POST'])
    def create_office():
        if request.method == 'GET':
            response = jsonify({
                "message": "Pollitical office retrieved successfully",
                "status": 200,
                "data": political_offices
            })
            response.status_code = 200
            return response
        if request.method == 'POST':
            data = request.get_json()  # getting a json object from request
            office_name = data['office_name']
            office_type = data['type']

            new_office = {}
            new_office["id"] = len(political_offices) + 1
            new_office["name"] = office_name
            new_office["type"] = office_type

            political_offices.append(new_office)

            response = jsonify({
                "message": "office created successfully",
                "status": 201,
                "data": political_offices
            })
            response.status_code = 201
            return response
   

    return app
