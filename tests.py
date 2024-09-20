import unittest
import json
from http.client import HTTPConnection


class TestPropertiesAPI(unittest.TestCase):
    """
    Class to test the properties API.
    Use unittest to perform tests on the application.
    """

    def setUp(self):
        """Configure the connection before each test."""
        self.conn = HTTPConnection('localhost', 8000)

    def test_get_properties(self):
        """Test: Obtain properties by city via POST"""
        data = {
            "city": "bogota"
        }
        json_data = json.dumps(data)
        headers = {'Content-Type': 'application/json'}
        self.conn.request('POST', '/properties', body=json_data, headers=headers)
        response = self.conn.getresponse()
        self.assertEqual(response.status, 200)
        response_data = response.read()
        properties = json.loads(response_data)
        self.assertEqual(len(properties), 8)

    def test_get_properties_by_year(self):
        """Test: Obtain properties by year"""
        data = {
            "year": "2018"
        }
        json_data = json.dumps(data)
        headers = {'Content-Type': 'application/json'}
        self.conn.request('POST', '/properties', body=json_data, headers=headers)
        response = self.conn.getresponse()
        self.assertEqual(response.status, 200)
        response_data = response.read()
        properties = json.loads(response_data)
        self.assertEqual(len(properties), 2)

    def test_get_properties_by_status(self):
        """Test: Obtain properties by status"""
        data = {
            "status": "en_venta"
        }
        json_data = json.dumps(data)
        headers = {'Content-Type': 'application/json'}
        self.conn.request('POST', '/properties', body=json_data, headers=headers)
        response = self.conn.getresponse()
        self.assertEqual(response.status, 200)
        response_data = response.read()
        properties = json.loads(response_data)
        self.assertEqual(len(properties), 8)

    def test_get_properties_by_status_and_year(self):
        """Test: Obtain properties by status and year"""
        data = {
            "status": "en_venta",
            "year": "2018"
        }
        json_data = json.dumps(data)
        headers = {'Content-Type': 'application/json'}
        self.conn.request('POST', '/properties', body=json_data, headers=headers)
        response = self.conn.getresponse()
        self.assertEqual(response.status, 200)
        response_data = response.read()
        properties = json.loads(response_data)
        self.assertEqual(len(properties), 1)

    def test_get_properties_by_status_and_city(self):
        """Test: Obtain properties by status and city"""
        data = {
            "status": "en_venta",
            "city": "bogota"
        }
        json_data = json.dumps(data)
        headers = {'Content-Type': 'application/json'}
        self.conn.request('POST', '/properties', body=json_data, headers=headers)
        response = self.conn.getresponse()
        self.assertEqual(response.status, 200)
        response_data = response.read()
        properties = json.loads(response_data)
        self.assertEqual(len(properties), 2)

    def test_get_properties_by_all_filters(self):
        """Test: Obtain properties using all parameters"""
        data = {
            "city": "bogota",
            "status": "en_venta",
            "year": "2018",
        }
        json_data = json.dumps(data)
        headers = {'Content-Type': 'application/json'}
        self.conn.request('POST', '/properties', body=json_data, headers=headers)
        response = self.conn.getresponse()
        self.assertEqual(response.status, 200)
        response_data = response.read()
        properties = json.loads(response_data)
        self.assertEqual(len(properties), 1)


    def tearDown(self):
        """Close the connection after each test."""
        self.conn.close()


if __name__ == '__main__':
    unittest.main()
