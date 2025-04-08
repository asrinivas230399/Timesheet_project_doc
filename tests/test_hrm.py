import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_employees_success(mocker):
    mocker.patch('requests.get', return_value=mocker.Mock(status_code=200, json=lambda: {'employees': []}))
    response = client.get('/hrm/employees')
    assert response.status_code == 200
    assert response.json() == {'employees': []}

def test_get_employees_failure(mocker):
    mocker.patch('requests.get', side_effect=requests.exceptions.RequestException('Error'))
    response = client.get('/hrm/employees')
    assert response.status_code == 200
    assert response.json() == {'error': 'Failed to fetch employees.'}

def test_assign_team_members_to_project():
    response = client.post('/hrm/projects/assign', json={'project_id': 1, 'employee_ids': [1, 2, 3]})
    assert response.status_code == 200
    assert response.json() == {'message': 'Team members assigned to project successfully.'}