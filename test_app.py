import unittest
from app import create_app

class FlaskTestCase(unittest.TestCase):
    """
    Test case for the Flask application.
    """

    def setUp(self):
        """
        Set up the test case by creating the Flask app and test client.
        """
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True

    def test_validate_success(self):
        """
        Test the successful validation endpoint.
        """
        response = self.client.post('/validate', json={
            "data": [
                {"var_name": "country", "category": "UK"},
                {"var_name": "age_group", "category": "30-50"}
            ]
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn("success", response.get_data(as_text=True))

    def test_validate_partial_failed(self):
        """
        Test the failed validation endpoint.
        """
        response = self.client.post('/validate', json={
            "data": [
                {"var_name": "country", "category": "UK"},
                {"var_name": "age_group", "category": "30-50"},
                {"var_name": "country", "category": "invalid"},
                {"var_name": "invalid", "category": "18-30"}
            ]
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn("failed", response.get_data(as_text=True))

    def test_validate_failed(self):
        """
        Test the failed validation endpoint.
        """
        response = self.client.post('/validate', json={
            "data": []
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn("No data", response.get_data(as_text=True))


    def test_get_factors_success(self):
        """
        Test the get_factors endpoint.
        """
        response = self.client.post('/get_factors', json={
            "data": [
                {"var_name": "country", "category": "UK"},
                {"var_name": "age_group", "category": "30-50"}
            ]
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(len(data["results"]), 2)
        self.assertEqual(data["results"][0]["factor"], 0.25)
        self.assertEqual(data["results"][1]["factor"], 0.33)

    def test_get_factors_failed(self):
        """
        Test the get_factors endpoint.
        """
        response = self.client.post('/get_factors', json={
            "data": [
                {"var_name": "country", "category": "UK"},
                {"var_name": "age_group", "category": "30-50"},
                {"var_name": "country", "category": "invalid"},
                {"var_name": "invalid", "category": "18-30"}
            ]
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(len(data["results"]), 4)
        self.assertEqual(data["results"][0]["factor"], 0.25)
        self.assertEqual(data["results"][1]["factor"], 0.33)
        self.assertEqual(data["results"][2]["factor"], "N/A")
        self.assertEqual(data["results"][3]["factor"], "N/A")

if __name__ == '__main__':
    unittest.main()