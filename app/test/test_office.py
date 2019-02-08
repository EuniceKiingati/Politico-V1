import json
from .base_test import BaseTest

class TestOffice(BaseTest):
    
    def test_create_office(self):
        response = self.client().post('/api/v1/offices', data=self.office_info,
                                      content_type='application/json')

        self.assertEqual(response.status_code, 201)
    
    def test_no_office_name(self):
        office_info = json.dumps({
            "office_name": "",
            "office_type": "sampleaddress",

        })
        response = self.client().post('/api/v1/offices', data=office_info,
                                      content_type='application/json')
        print(response.data)
        self.assertEqual(response.status_code, 400)
    
    def test_taken_office_name(self):
        office_info = json.dumps({
        "office_name": "sampleofficename",
            "office_type": "sampletype"

        })
        response = self.client().post('/api/v1/offices', data=office_info,
                                      content_type='application/json')
    
        self.assertEqual(response.status_code, 400)