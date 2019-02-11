users = []
political_parties = []
political_offices = []

class SaveUser():
    def __init__(self, data):
        self.data = data

    def save(self):
        new_user = {}
        new_user['user_id'] = len(users) + 1
        new_user["username"] = self.data['username']
        new_user["email"] = self.data['email']
        new_user["password"] = self.data['password']
        users.append(new_user)


class Party():
    def __init__(self, data):
        self.data = data

    def save(self):
        new_party = {}
        new_party["id"] = len(political_parties) + 1
        new_party["party_name"] = self.data['party_name']
        new_party["hqadress"] = self.data['hqaddress']
        new_party["logoUrl"] = self.data['logoUrl']
        political_parties.append(new_party)


class Office():
    def __init__(self, data):
        self.data = data

    def save(self):
        new_office = {}
        new_office["id"] = len(political_offices) + 1
        new_office["office_name"] = self.data['office_name']
        new_office["office_type"] = self.data['office_type']

        political_offices.append(new_office)
        