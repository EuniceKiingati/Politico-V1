import re
from flask import jsonify, abort
from app.api.v1.models import political_offices


def bad_request(message):
    response = jsonify({
        "error": message,
        "status": 400,
    })
    response.status_code = 400
    abort(response)


class ValidateOffice():
    def __init__(self, data):
        self.data = data

    def validate_create(self):
        if not self.data:
            message = "You must provide create_office data"
            return bad_request(message)
        office_name = self.data['office_name']
        if office_name == "":
            message = "office_name is missing"
            return bad_request(message)
        for office in political_offices:
            if office_name == office['office_name']:
                message = "office name {} already taken".format(
                    office_name)
                return bad_request(message)
        if type(office_name) != str:
            message = "office_name must be a string"
            return bad_request(message)
