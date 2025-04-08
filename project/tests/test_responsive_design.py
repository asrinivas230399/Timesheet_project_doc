import pytest
from httpx import AsyncClient
from app.main import app

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
