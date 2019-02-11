from flask import Flask, jsonify, request, abort
import json
from .utils.user_utils import UserValidation
from .utils.party_utils import ValidateParty
from .utils.office_utils import ValidateOffice
from .models import (users, SaveUser, political_parties,
                     Party, political_offices, Office)


def bad_request(message):
    response = jsonify({
        "message": message,
        "status": 400,
    })
    response.status_code = 400
    return response


def create_app():
    app = Flask(__name__)

    @app.route('/api/v1/users', methods=['POST'])
    def sign_up():
        data = request.get_json()
        validate = UserValidation(data)
        validate.validate_signup()
        new_user = SaveUser(data)
        new_user.save()

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
        validate = UserValidation(data)
        return validate.validate_login()

    @app.route('/api/v1/parties', methods=['POST'])
    def create_parties():
        data = request.get_json()  # getting a json object from request
        validate = ValidateParty(data)
        validate.validate_create()
        new_party = Party(data)
        new_party.save()
        response = jsonify({
            "message": "party created successfully",
            "status": 201,
            "data": political_parties
        })
        response.status_code = 201
        return response

    @app.route('/api/v1/parties', methods=['GET'])
    def get_parties():
        response = jsonify({
            "message": "Political parties retrieved successfully",
            "status": 200,
            "data": political_parties
        })
        response.status_code = 200
        return response

    @app.route('/api/v1/parties/<int:party_id>', methods=['GET'])
    def single_political_party(party_id):
        for party in political_parties:
            if party['id'] == party_id:
                political_parties.remove(party)

                response = jsonify({
                    "message": "Political parties deleted successfully",
                    "status": 200,
                    "data": political_parties
                })
                response.status_code = 200
                return response
        response = jsonify({
            "message": "Party not found",
            "status": 404,
        })
        response.status_code = 404
        return response

    @app.route('/api/v1/parties/<int:party_id>', methods=['DELETE'])
    def delete_political_party(party_id):
        for party in political_parties:
            if party['id'] == party_id:
                response = jsonify({
                    "status": 200,
                    "data": party
                })
                response.status_code = 200
                return response
        response = jsonify({
            "message": "Party not found",
            "status": 404,
        })
        response.status_code = 404
        return response

    @app.route('/api/v1/parties/<int:party_id>/name', methods=['PATCH'])
    def edit_party_name(party_id):

        data = request.get_json()  # data being passed
        party_name = data['party_name']
        for party in political_parties:
            if party_name == party["party_name"] and party['id'] != party_id:
                message = "party name {} already taken".format(party_name)
                return bad_request(message)
            if party['id'] == party_id:
                party['name'] = party_name

                response = jsonify({
                    "message": "Pollitical party updated successfully",
                    "status": 200,
                    "data": party
                })
                response.status_code = 200
                return response
        response = json ({"message":"Party not found",
            "status": 404
        })
        response.status_code = 404
        return response

    @app.route('/api/v1/offices', methods=['GET'])
    def get_offices():
        response = jsonify({
            "message": "Pollitical office retrieved successfully",
            "status": 200,
            "data": political_offices
        })
        response.status_code = 200
        return response

    @app.route('/api/v1/offices', methods=['POST'])
    def create_office():
        data = request.get_json()  # getting a json object from request
        validate = ValidateOffice(data)
        validate.validate_create()
        new_office = Office(data)
        new_office.save()

        response = jsonify({
            "message": "office created successfully",
            "status": 201,
            "data": political_offices
        })
        response.status_code = 201
        return response

    @app.route('/api/v1/offices/<int:office_id>', methods=['GET'])
    def single_political_office(office_id):
        for office in political_offices:

            if office['id'] == office_id:
                response = jsonify({
                    "status": 200,
                    "data": office
                })
                response.status_code = 200
                return response
        response = jsonify({
            "message": "Office not found",
            "status": 404,
        })
        response.status_code = 404
        return response

    return app
