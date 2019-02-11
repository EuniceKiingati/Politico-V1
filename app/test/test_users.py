import json
from .base_test import BaseTest


class TestUser(BaseTest):

    def test_create_user(self):
        response = self.client().post('/api/v1/users', data=self.user_info,
                                      content_type='application/json')

        self.assertEqual(response.status_code, 201)

    def test_signup_no_username(self):
        user_info = json.dumps({
            "username": "",
            "email": "sampleemail",
            "password": "Password2#",

        })
        response = self.client().post('/api/v1/users', data=user_info,
                                      content_type='application/json')

        self.assertEqual(response.status_code, 400)

    def test_signup_taken_username(self):
        user_info = json.dumps({
            "username": "sampleusername",
            "email": "sampleemail",
            "password": "Yunis",

            "username": "sampleusername",
            "email": "sampleemail",
            "password": "Yunis",

        })
        response = self.client().post('/api/v1/users', data=user_info,
                                      content_type='application/json')

        self.assertEqual(response.status_code, 400)

    def test_signup_no_password(self):
        user_info = json.dumps({
            "username": "sampleusername",
            "email": "sampleemail",
            "password": "",

        })
        response = self.client().post('/api/v1/users', data=user_info,
                                      content_type='application/json')

        self.assertEqual(response.status_code, 400)

    def test_signup_caps_password(self):
        user_info = json.dumps({
            "username": "sampleusername",
            "email": "sampleemail",
            "password": "yuns8888#",

        })
        response = self.client().post('/api/v1/users', data=user_info,
                                      content_type='application/json')

        self.assertEqual(response.status_code, 400)

    def test_signup_number_password(self):
        user_info = json.dumps({
            "username": "sampleusername",
            "email": "sampleemail",
            "password": "Yunisabcde",

        })
        response = self.client().post('/api/v1/users', data=user_info,
                                      content_type='application/json')

        self.assertEqual(response.status_code, 400)

    def test_signup_special_password(self):
        user_info = json.dumps({
            "username": "sampleusername",
            "email": "sampleemail",
            "password": "Yunisab2",

        })
        response = self.client().post('/api/v1/users', data=user_info,
                                      content_type='application/json')

        self.assertEqual(response.status_code, 400)

    def test_signup_length_password(self):
        user_info = json.dumps({
            "username": "sampleusername",
            "email": "sampleemail",
            "password": "Yunis",

        })
        response = self.client().post('/api/v1/users', data=user_info,
                                      content_type='application/json')

        self.assertEqual(response.status_code, 400)

    def test_signup_string_password(self):
        user_info = json.dumps({
            "username": "sampleusername",
            "email": "sampleemail",
            "password": "2",

        })
        response = self.client().post('/api/v1/users', data=user_info,
                                      content_type='application/json')

        self.assertEqual(response.status_code, 400)

    def test_signup_lowercase_password(self):
        user_info = json.dumps({
            "username": "sampleusername",
            "email": "sampleemail",
            "password": "YUNIS2@",

        })
        response = self.client().post('/api/v1/users', data=user_info,
                                      content_type='application/json')

        self.assertEqual(response.status_code, 400)

    def test_Login(self):
        self.client().post('/api/v1/users', data=self.user_info,
                           content_type='application/json')
        response = self.client().post('/api/v1/users/login', data=self.user_info,
                                      content_type="application/json")

        self.assertEqual(response.status_code, 200)

    def test_invalid_login(self):
        resp = self.client().post('/api/v1/users/login', data=self.user_info,
                                  content_type="application/json")
        self.assertEqual(resp.status_code, 401)

    def test_login_no_username(self):
        user_info = json.dumps({
            "username": "",
            "email": "sampleemail",
            "password": "Password2#"

        })
        response = self.client().post('/api/v1/users', data=user_info,
                                      content_type='application/json')

        self.assertEqual(response.status_code, 400)

    def test_login_no_password(self):
        user_info = json.dumps({
            "username": "yunis",
            "email": "sampleemail",
            "password": ""

        })
        response = self.client().post('/api/v1/users', data=user_info,
                                      content_type='application/json')

        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
