from fastapi import APIRouter
import requests
from app.config import settings
from app.clients.hrm_client import HRMClient
import logging

router = APIRouter()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

hrm_api_url = settings.HRM_API_URL
hrm_client = HRMClient()

@router.get("/employees")
async def get_employees():
    try:
        response = requests.get(f"{hrm_api_url}/employees")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching employees: {e}")
        return {"error": "Failed to fetch employees."}

@router.post("/projects/assign")
async def assign_team_members_to_project(project_id: int, employee_ids: list[int]):
    try:
        # Endpoint to assign team members to a project
        # Here you would implement the logic to assign employees to a project
        # For example, updating the project assignment in a database
        return {"message": "Team members assigned to project successfully."}
    except Exception as e:
        logger.error(f"Error assigning team members to project: {e}")
        return {"error": "Failed to assign team members to project."}

@router.post("/projects/assign-from-hrm")
async def assign_team_members_from_hrm(project_id: int):
    try:
        employees = hrm_client.fetch_data("employees")
        if employees:
            # Logic to filter and assign employees to the project based on HRM data
            # For example, assign all employees to the project
            employee_ids = [employee['id'] for employee in employees]
            # Implement the logic to assign these employees to the project
            return {"message": "Team members assigned to project successfully from HRM data."}
        else:
            logger.error("Failed to fetch employees from HRM.")
            return {"error": "Failed to fetch employees from HRM."}
    except Exception as e:
        logger.error(f"Failed to assign team members from HRM: {str(e)}")
        return {"error": f"Failed to assign team members from HRM: {str(e)}"}