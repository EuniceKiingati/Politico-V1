import re
from flask import jsonify, abort
from app.api.v1.models import political_parties


def bad_request(message):
    response = jsonify({
        "error": message,
        "status": 400,
    })
    response.status_code = 400
    abort(response)


class ValidateParty():
    def __init__(self, data):
        self.data = data

    def validate_create(self):
        if not self.data:
            message = "You must provide create_party data"
            return bad_request(message)
        party_name = self.data['party_name']
        if party_name == "":
            message = "party_name is missing"
            return bad_request(message)
        for party in political_parties:
            if party_name == party["party_name"]:
                message = "party_name {} already taken".format(party_name)
                return bad_request(message)
        if type(party_name) != str:
            message = "party name must be a string"
            return bad_request(message)
