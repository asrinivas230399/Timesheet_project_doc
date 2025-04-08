import requests
from app.config import settings

class TimeTrackingClient:
    def __init__(self, api_url: str = settings.TIME_TRACKING_API_URL):
        self.api_url = api_url

    def get_headers(self):
        # Example method to get headers, including authentication
        return {
            "Authorization": "Bearer YOUR_ACCESS_TOKEN",
            "Content-Type": "application/json"
        }

    def fetch_data(self, endpoint: str):
        try:
            response = requests.get(f"{self.api_url}/{endpoint}", headers=self.get_headers())
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")
        return None

    def sync_time_data(self):
        # Fetch and update time tracking data for real-time synchronization
        data = self.fetch_data("entries")
        if data:
            # Here you would implement the logic to update your local database or state
            print("Time tracking data synchronized successfully.")
        else:
            print("Failed to synchronize time tracking data.")