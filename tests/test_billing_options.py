import unittest
from fastapi.testclient import TestClient
from billing_service import BillingService, FixedRate, TimeAndMaterial
from main import app  # Assuming the FastAPI app is in main.py

class TestBillingOptions(unittest.TestCase):
    def setUp(self):
        self.billing_service = BillingService()
        self.client = TestClient(app)

    def test_fixed_rate_model(self):
        fixed_rate = FixedRate(rate=100.0, currency='USD')
        self.assertEqual(fixed_rate.rate, 100.0)
        self.assertEqual(fixed_rate.currency, 'USD')

    def test_time_and_material_model(self):
        time_and_material = TimeAndMaterial(hourly_rate=50.0, currency='USD', estimated_hours=10.0)
        self.assertEqual(time_and_material.hourly_rate, 50.0)
        self.assertEqual(time_and_material.currency, 'USD')
        self.assertEqual(time_and_material.estimated_hours, 10.0)

    def test_toggle_billing_option_fixed_rate(self):
        project_id = 'project1'
        data = {'rate': 100.0, 'currency': 'USD'}
        self.billing_service.toggle_billing_option(project_id, 'fixed_rate', data)
        option = self.billing_service.retrieve_billing_option(project_id)
        self.assertIsInstance(option, FixedRate)
        self.assertEqual(option.rate, 100.0)

    def test_toggle_billing_option_time_and_material(self):
        project_id = 'project2'
        data = {'hourly_rate': 50.0, 'currency': 'USD', 'estimated_hours': 20.0}
        self.billing_service.toggle_billing_option(project_id, 'time_and_material', data)
        option = self.billing_service.retrieve_billing_option(project_id)
        self.assertIsInstance(option, TimeAndMaterial)
        self.assertEqual(option.hourly_rate, 50.0)

    def test_get_billing_option_endpoint(self):
        project_id = 'project1'
        data = {'rate': 100.0, 'currency': 'USD'}
        self.billing_service.toggle_billing_option(project_id, 'fixed_rate', data)
        response = self.client.get(f'/billing/{project_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'rate': 100.0, 'currency': 'USD'})

    def test_set_billing_option_endpoint(self):
        project_id = 'project3'
        data = {
            'option_type': 'fixed_rate',
            'data': {'rate': 150.0, 'currency': 'USD'}
        }
        response = self.client.post(f'/billing/{project_id}', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'message': 'Billing option set successfully'})

if __name__ == '__main__':
    unittest.main()