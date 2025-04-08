from fastapi import APIRouter
import requests
from app.config import settings
from app.clients.time_tracking_client import TimeTrackingClient
import logging

router = APIRouter()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

time_tracking_api_url = settings.TIME_TRACKING_API_URL

time_tracking_client = TimeTrackingClient()

@router.get("/entries")
async def get_time_entries():
    try:
        response = requests.get(f"{time_tracking_api_url}/entries")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching time entries: {e}")
        return {"error": "Failed to fetch time entries."}

@router.post("/sync")
async def sync_time_entries():
    try:
        time_tracking_client.sync_time_data()
        return {"message": "Time tracking data synchronization triggered."}
    except Exception as e:
        logger.error(f"Error synchronizing time tracking data: {e}")
        return {"error": "Failed to synchronize time tracking data."}

@router.get("/tasks/time-spent")
async def get_time_spent_on_tasks():
    try:
        response = requests.get(f"{time_tracking_api_url}/tasks/time-spent")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching time spent on tasks: {e}")
        return {"error": "Failed to fetch time spent on tasks."}

@router.post("/integrations/configure")
async def configure_time_tracking_integration(integration_data: dict):
    try:
        # Implement the logic to configure the integration
        return {"message": "Time tracking tool integration configured successfully."}
    except Exception as e:
        logger.error(f"Error configuring time tracking integration: {e}")
        return {"error": "Failed to configure time tracking integration."}