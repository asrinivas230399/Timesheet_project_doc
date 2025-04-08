import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_read_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert "Hello" in response.text

@pytest.mark.asyncio
async def test_get_project_details():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/project")
    assert response.status_code == 200
    assert "Project Details" in response.text

@pytest.mark.asyncio
async def test_get_task_updates():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/task")
    assert response.status_code == 200
    assert "Task Updates" in response.text

@pytest.mark.asyncio
async def test_update_task():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/task/update", data={"task_id": 1, "status": "In Progress"})
    assert response.status_code == 303  # Redirect after update

@pytest.mark.asyncio
async def test_responsive_design_mobile():
    headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X)"}
    async with AsyncClient(app=app, base_url="http://test", headers=headers) as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert "mobile" in response.headers['X-Device-Type']

@pytest.mark.asyncio
async def test_responsive_design_tablet():
    headers = {"User-Agent": "Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X)"}
    async with AsyncClient(app=app, base_url="http://test", headers=headers) as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert "tablet" in response.headers['X-Device-Type']

@pytest.mark.asyncio
async def test_responsive_design_desktop():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    async with AsyncClient(app=app, base_url="http://test", headers=headers) as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert "desktop" in response.headers['X-Device-Type']
