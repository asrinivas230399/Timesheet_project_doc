import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_stylesheet_mobile():
    headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X)"}
    async with AsyncClient(app=app, base_url="http://test", headers=headers) as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert "lightgreen" in response.text  # Check for mobile background color

@pytest.mark.asyncio
async def test_stylesheet_tablet():
    headers = {"User-Agent": "Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X)"}
    async with AsyncClient(app=app, base_url="http://test", headers=headers) as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert "lightcoral" in response.text  # Check for tablet background color

@pytest.mark.asyncio
async def test_stylesheet_desktop():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    async with AsyncClient(app=app, base_url="http://test", headers=headers) as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert "lightblue" in response.text  # Check for desktop background color
