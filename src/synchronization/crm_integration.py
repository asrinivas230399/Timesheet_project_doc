import requests

class CRMIntegration:
    def __init__(self, api_url: str, api_key: str):
        self.api_url = api_url
        self.api_key = api_key

    def fetch_customers(self) -> list:
        """Fetch customer data from the CRM system."""
        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = requests.get(f'{self.api_url}/customers', headers=headers)
        response.raise_for_status()
        return response.json()

    def synchronize_customers(self):
        """Synchronize customer data with the local database."""
        customers = self.fetch_customers()
        for customer in customers:
            self.update_or_create_customer(customer)

    def update_or_create_customer(self, customer_data: dict):
        """Update an existing customer or create a new one in the local database."""
        # This is a placeholder for actual database logic
        print(f"Synchronizing customer: {customer_data['name']}")

# Example usage
if __name__ == "__main__":
    crm_integration = CRMIntegration(api_url="https://api.example-crm.com", api_key="your_api_key_here")
    crm_integration.synchronize_customers()