import unittest
import json
from app.api.v1.models import users
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

    def tearDown(self):
        users.clear()
