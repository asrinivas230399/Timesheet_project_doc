import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_time_entries_success(mocker):
    mocker.patch('requests.get', return_value=mocker.Mock(status_code=200, json=lambda: {'data': 'some data'}))
    response = client.get('/time-tracking/entries')
    assert response.status_code == 200
    assert response.json() == {'data': 'some data'}

def test_get_time_entries_failure(mocker):
    mocker.patch('requests.get', side_effect=requests.exceptions.RequestException('Error'))
    response = client.get('/time-tracking/entries')
    assert response.status_code == 200
    assert response.json() == {'error': 'Failed to fetch time entries.'}

def test_sync_time_entries_success(mocker):
    mocker.patch('app.clients.time_tracking_client.TimeTrackingClient.sync_time_data', return_value=None)
    response = client.post('/time-tracking/sync')
    assert response.status_code == 200
    assert response.json() == {'message': 'Time tracking data synchronization triggered.'}

def test_sync_time_entries_failure(mocker):
    mocker.patch('app.clients.time_tracking_client.TimeTrackingClient.sync_time_data', side_effect=Exception('Error'))
    response = client.post('/time-tracking/sync')
    assert response.status_code == 200
    assert response.json() == {'error': 'Failed to synchronize time tracking data.'}