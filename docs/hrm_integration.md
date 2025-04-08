# HRM Integration Documentation

## Setup Instructions
1. Obtain the necessary API credentials for the HRM service.
2. Set the `HRM_API_URL` in your environment variables or in the `app/config.py` file.
3. Install the required dependencies using `pip install -r requirements.txt`.

## Usage Guidelines
- **Get Employees**: Use the `/hrm/employees` endpoint to fetch a list of employees.
- **Assign Team Members to Project**: Use the `/hrm/projects/assign` endpoint to assign employees to a project by providing the project ID and a list of employee IDs.

## Troubleshooting
- If you encounter errors while fetching data, ensure the API URL is correct and the service is reachable.
- Check the logs for any error messages that can provide more context on the issue.
- Ensure that your API credentials are valid and have the necessary permissions.