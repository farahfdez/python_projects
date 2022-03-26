import unittest

from flask import json

from api_rest import app


class ApiRestTest(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()

    def test_add_endpoint(self):
        response = self.app.post(
            '/suma',
            data=json.dumps({'v1': [2], 'v2': [1]}),
            content_type='application/json',
        )
        self.assertEqual(200, response.status_code)
        self.assertEqual([3], json.loads(response.get_data(as_text=True))["result"])

    def test_subtract_endpoint(self):
        response = self.app.post(
            '/resta',
            data=json.dumps({'v1': [2], 'v2': [1]}),
            content_type='application/json',
        )
        self.assertEqual(200, response.status_code)
        self.assertEqual([1], json.loads(response.get_data(as_text=True))["result"])

    def test_multiply_endpoint(self):
        response = self.app.post(
            '/mult',
            data=json.dumps({'v1': [2], 'v2': [1]}),
            content_type='application/json',
        )
        self.assertEqual(200, response.status_code)
        self.assertEqual([2], json.loads(response.get_data(as_text=True))["result"])

    def test_divide_endpoint(self):
        response = self.app.post(
            '/divis',
            data=json.dumps({'v1': [2], 'v2': [2]}),
            content_type='application/json',
        )
        self.assertEqual(200, response.status_code)
        self.assertEqual([1], json.loads(response.get_data(as_text=True))["result"])

    def test_bad_request_if_json_is_invalid(self):
        response = self.app.post(
            '/divis',
            data=json.dumps({'v': [2], 'v2': [2]}),
            content_type='application/json',
        )
        self.assertEqual(400, response.status_code)
        self.assertEqual("Lists of values should be named v1 and v2",
                         json.loads(response.get_data(as_text=True))["error"])

    def test_invalid_data_type(self):
        response = self.app.post(
            '/divis',
            data=json.dumps({'v1': ["A"], 'v2': [2]}),
            content_type='application/json',
        )
        self.assertEqual(500, response.status_code)
        self.assertEqual("Invalid data type", json.loads(response.get_data(as_text=True))["error"])

    def test_list_length(self):
        response = self.app.post(
            '/divis',
            data=json.dumps({'v1': [2, 3], 'v2': [2]}),
            content_type='application/json',
        )
        self.assertEqual(500, response.status_code)
        self.assertEqual("Lists of values should have same length",
                         json.loads(response.get_data(as_text=True))["error"])

    def test_invalid_division(self):
        response = self.app.post(
            '/divis',
            data=json.dumps({'v1': [2], 'v2': [0]}),
            content_type='application/json',
        )
        self.assertEqual(500, response.status_code)
        self.assertEqual("Invalid division by zero", json.loads(response.get_data(as_text=True))["error"])


if __name__ == '__main__':
    unittest.main()
