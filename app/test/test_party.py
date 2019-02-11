import json
from .base_test import BaseTest

class TestParty(BaseTest):
    
    def test_create_party(self):
        response = self.client().post('/api/v1/parties', data=self.party_info,
                                      content_type='application/json')

        self.assertEqual(response.status_code, 201)
    
    def test_no_party_name(self):
        party_info = json.dumps({
            "party_name": "",
            "hqaddress": "sampleaddress",
            "logoUrl": "sampleurl"

        })
        response = self.client().post('/api/v1/parties', data=party_info,
                                      content_type='application/json')

        self.assertEqual(response.status_code, 400)
    
    def test_taken_party_name(self):
        party_info = json.dumps({
            "party_name": "samplepartyname",
            "hqaddress": "sampleaddress",
            "logoUrl": "sampleurl"

        })
        self.client().post('/api/v1/parties', data=party_info,
                                      content_type='application/json')
        response = self.client().post('/api/v1/parties', data=party_info,
                                      content_type='application/json')

        self.assertEqual(response.status_code, 400)

    