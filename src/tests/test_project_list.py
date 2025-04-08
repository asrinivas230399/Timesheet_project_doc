import pytest
from httpx import AsyncClient
from fastapi import FastAPI
from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from src.routers.project_router import router
import time


@pytest.fixture
async def app() -> FastAPI:
    app = FastAPI()
    app.include_router(router)
    return app


@pytest.fixture
async def client(app: FastAPI) -> AsyncClient:
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client


@pytest.mark.asyncio
async def test_get_projects(client: AsyncClient):
    start_time = time.time()
    response = await client.get("/projects")
    end_time = time.time()
    assert response.status_code == HTTP_200_OK
    assert isinstance(response.json(), list)
    assert (end_time - start_time) < 1  # Load time should be less than 1 second


@pytest.mark.asyncio
async def test_get_project(client: AsyncClient):
    response = await client.get("/projects/1")
    assert response.status_code == HTTP_200_OK
    assert response.json()["id"] == 1


@pytest.mark.asyncio
async def test_get_project_not_found(client: AsyncClient):
    response = await client.get("/projects/999")
    assert response.status_code == HTTP_404_NOT_FOUND
    assert response.json()["error"] == "Project not found"


@pytest.mark.asyncio
async def test_create_project(client: AsyncClient):
    new_project = {"name": "Project Gamma"}
    response = await client.post("/projects", json=new_project)
    assert response.status_code == HTTP_200_OK
    assert response.json()["name"] == "Project Gamma"


@pytest.mark.asyncio
async def test_update_project(client: AsyncClient):
    updated_project = {"name": "Project Alpha Updated"}
    response = await client.put("/projects/1", json=updated_project)
    assert response.status_code == HTTP_200_OK
    assert response.json()["name"] == "Project Alpha Updated"


@pytest.mark.asyncio
async def test_delete_project(client: AsyncClient):
    response = await client.delete("/projects/1")
    assert response.status_code == HTTP_200_OK
    assert response.json()["message"] == "Project deleted"


@pytest.mark.asyncio
async def test_concurrent_requests(client: AsyncClient):
    async def get_projects():
        response = await client.get("/projects")
        assert response.status_code == HTTP_200_OK

    async def create_project():
        new_project = {"name": "Project Delta"}
        response = await client.post("/projects", json=new_project)
        assert response.status_code == HTTP_200_OK

    tasks = [get_projects(), create_project()]
    await asyncio.gather(*tasks)  # Test concurrency by running tasks in parallel