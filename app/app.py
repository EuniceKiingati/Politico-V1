# from flask import Flask, jsonify, request, abort
# import json
# import re


# def bad_request(message):
#     response = jsonify({
#                 "message": message,
#                 "status": 400,
#                 })
#     response.status_code = 400
#     return response

# def create_app():
#     app = Flask(__name__)
#     users = []
#     political_parties = []
#     political_offices = []


#     @app.route('/api/v1/users', methods=['POST'])
#     def sign_up():
#         data = request.get_json()
#         if not data:
#             message= "You must provide signup data"
#             return bad_request(message)
            
#         username = data['username']
#         if username =="":
#             message='Username is missing'
#             return bad_request(message)
#         for user in users:
#             if username == user["username"]:
#                 message= "username {} already taken".format(username)
#                 return bad_request(message)
#         if type(username) != str:
#                 message= "Username must be a string"
#                 return bad_request(message)
#         password= data['password']
#         if password == "":
#             message = "Password is missing"
#             return bad_request(message)
#         if type(password) != str:
#             message = "Password must be a string"
#             return bad_request(message)
#         if len(password) <= 6 or len(password) > 12:
#             message = "Password must be at least 6 and at most 10 ch long"
#             return bad_request(message)
#         elif not any(char.isdigit() for char in password):
#             message = "Password must have a digit"
#             return bad_request(message)
#         elif not any(char.isupper() for char in password):
#             message = "Password must have an upper case character"
#             return bad_request(message)
#         elif not any(char.islower() for char in password):
#             message = "Password must have a lower case character"
#             return bad_request(message)
#         elif not re.search("[#@$]", password):
#             message = "Password must have one of the special charater [#@$]"
#             return bad_request(message)
        
#         new_user = {}
#         new_user['user_id'] = len(users) + 1
#         new_user["username"] = username
#         new_user["email"] = data['email']
#         new_user["password"] = data['password']
#         users.append(new_user)

#         response = jsonify({
#             "message": "user created successfully",
#             "status": 201,
#             "data": users
#         })
#         response.status_code = 201
#         return response

#     @app.route('/api/v1/users/login', methods=['POST'])
#     def login():
#         data = request.get_json()  # getting a json object from request
#         if not data:
            
#             message = "You must provide login data"
#             return bad_request(message)
           
#         username = data['username'] # gets the value that the key represents
#         if username =="":
#             message='Username is missing'
#             return bad_request(message)
#         password = data['password']
#         if password == "":
#             message = "Password is missing"
#             return bad_request(message)
#         for user in users:
#             if user['username'] == username and user['password'] == password:  # to loo
#                 response = jsonify({
#                     "message": "User login successful",
#                     "status": 200,
#                     "data": user
#                 })
#                 response.status_code = 200
#                 return response
#         response = jsonify({
#             "message": "User login failed, Check your credentials",
#             "status": 401,  # not  found
#         })
#         response.status_code = 401
#         return response

#     @app.route('/api/v1/parties', methods=['POST', 'GET'])
#     def create_party():
#         if request.method == 'GET':
#             response = jsonify({
#                 "message": "Political parties retrieved successfully",
#                 "status": 200,
#                 "data": political_parties
#             })
#             response.status_code = 200
#             return response
#         if request.method == 'POST':
#             data = request.get_json()  # getting a json object from request
#             if not data:
#                 message= "You must provide create_party data"
#                 return bad_request(message)
#             party_name = data['party_name']
#             if party_name =="":
#                 message = "party_name is missing"
#                 return bad_request(message)
#             for party in political_parties:
#                 if party_name == party["party_name"]:
#                     message = "party_name {} already taken".format(party_name)
#                     return bad_request(message)
#             if type(party_name) != str:
#                 message = "party name must be a string"
#                 return bad_request(message)
#             hqaddress = data['hqaddress']
#             logoUrl = data['logoUrl']
#             new_party = {}
#             new_party["id"] = len(political_parties) + 1
#             new_party["party_name"] = party_name
#             new_party["hqadress"] = hqaddress
#             new_party["logoUrl"] = logoUrl
#             political_parties.append(new_party)

#             response = jsonify({
#                 "message": "party created successfully",
#                 "status": 201,
#                 "data": political_parties
#             })
#             response.status_code = 201
#             return response

#     @app.route('/api/v1/parties/<int:party_id>', methods=['GET', 'DELETE'])
#     def single_political_party(party_id):
#         if request.method == 'DELETE':
#             for party in political_parties:
#                 if party['id'] == party_id:
#                     political_parties.remove(party)

#                     response = jsonify({
#                         "message": "Political parties deleted successfully",
#                         "status": 200,
#                         "data": political_parties
#                     })
#                     response.status_code = 200
#                     return response
#             response = jsonify({
#                 "message": "invalid id",
#                 "status": 404,
#             })
#             response.status_code = 404
#             return response
#         if request.method == 'GET':
#             for party in political_parties:
#                 if party['id'] == party_id:
#                     response = jsonify({
#                         "status": 200,
#                         "data": party
#                     })
#                     response.status_code = 200
#                     return response
#             response = jsonify({
#                 "message": "invalid id",
#                 "status": 404,
#             })
#             response.status_code = 404
#             return response

#     @app.route('/api/v1/parties/<int:party_id>/name', methods=['PATCH'])
#     def edit_party_name(party_id):

#         data = request.get_json()  # data being passed
#         party_name = data['party_name']
#         for party in political_parties:
#             if party_name == party["party_name"]:
#                 message= "party name {} already taken".format(party_name)
#                 return bad_request(message)
#             if party['id'] == party_id:
#                 party['name'] = party_name

#                 response = jsonify({
#                     "message": "Pollitical party updated successfully",
#                     "status": 200,
#                     "data": party
#                 })
#                 response.status_code = 200
#                 return response
#         response = jsonify({
#             "message": "invalid id",
#             "status": 404
#         })
#         response.status_code = 404
#         return response

#     @app.route('/api/v1/offices', methods=['GET', 'POST'])
#     def create_office():
#         if request.method == 'GET':
#             response = jsonify({
#                 "message": "Pollitical office retrieved successfully",
#                 "status": 200,
#                 "data": political_offices
#             })
#             response.status_code = 200
#             return response
#         if request.method == 'POST':
#             data = request.get_json()  # getting a json object from request
#             if not data:
#                 message= "You must provide create_office data"
#                 return bad_request(message)    
#             office_name = data['office_name']
#             if office_name =="":
#                 message = "office_name is missing"
#                 return bad_request(message) 
#             for office in political_offices:
#                 if office_name == office["office_name"]:
#                     message = "office name {} already taken".format(office_name)
#                     return bad_request(message) 
#             if type(office_name) != str:
#                 message = "office_name must be a string"
#                 return bad_request(message) 
#             office_type = data['type']

#             new_office = {}
#             new_office["id"] = len(political_offices) + 1
#             new_office["name"] = office_name
#             new_office["type"] = office_type

#             political_offices.append(new_office)

#             response = jsonify({
#                 "message": "office created successfully",
#                 "status": 201,
#                 "data": political_offices
#             })
#             response.status_code = 201
#             return response

#     @app.route('/api/v1/offices/<int:office_id>', methods=['GET'])
#     def single_political_office(office_id):
#         for office in political_offices:

#             if office['id'] == office_id:
#                 response = jsonify({
#                     "status": 200,
#                     "data": office
#                 })
#                 response.status_code = 200
#                 return response
#         response = jsonify({
#             "message": "invalid id",
#             "status": 404,
#         })
#         response.status_code = 404
#         return response

#     return app
