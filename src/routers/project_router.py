from fastapi import APIRouter, Query
from typing import List, Optional
from src.services.project_service import get_projects, create_project, get_project, update_project, delete_project

router = APIRouter()

@router.get("/projects", response_model=List[dict])
async def get_projects_endpoint(
    name: Optional[str] = Query(None, description="Filter by project name"),
    skip: int = Query(0, ge=0, description="Number of projects to skip"),
    limit: int = Query(10, ge=1, description="Maximum number of projects to return")
):
    """Fetch the list of projects with optional filtering and pagination"""
    return await get_projects(name=name, skip=skip, limit=limit)

@router.post("/projects", response_model=dict)
async def create_project_endpoint(project: dict):
    """Create a new project"""
    return await create_project(project)

@router.get("/projects/{project_id}", response_model=dict)
async def get_project_endpoint(project_id: int):
    """Fetch a single project by ID"""
    return await get_project(project_id)

@router.put("/projects/{project_id}", response_model=dict)
async def update_project_endpoint(project_id: int, updated_project: dict):
    """Update an existing project"""
    return await update_project(project_id, updated_project)

@router.delete("/projects/{project_id}", response_model=dict)
async def delete_project_endpoint(project_id: int):
    """Delete a project by ID"""
    return await delete_project(project_id)
