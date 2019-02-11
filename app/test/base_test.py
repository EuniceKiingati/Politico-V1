import unittest
import json
from app.api.v1.models import users, political_parties, political_offices
from app.api.v1.views import create_app


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.user_info = json.dumps({
            "username": "sampleusername",
            "email": "sampleemail",
            "password": "Password2#",
            "isadmin": "true"
        })
        self.party_info = json.dumps({
            "party_name": "sampleusername",
            "hqaddress": "sampleaddress",
            "logoUrl": "https://cdn1-www.comingsoon.net/assets/uploads/2018/09/dragon-3-768x432.jpg"

        })
        self.office_info = json.dumps({
            "office_name": "sampleofficename",
            "office_type": "sampletype"

        })

    def tearDown(self):
        users.clear()
        political_parties.clear
