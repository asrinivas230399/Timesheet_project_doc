from fastapi import APIRouter, Query
from typing import List, Optional
from .project_list import get_projects

router = APIRouter()

# In-memory project list for demonstration purposes
projects = [
    {"id": 1, "name": "Project Alpha"},
    {"id": 2, "name": "Project Beta"}
]

@router.get("/projects", response_model=List[dict])
async def get_projects_endpoint(
    name: Optional[str] = Query(None, description="Filter by project name"),
    skip: int = Query(0, ge=0, description="Number of projects to skip"),
    limit: int = Query(10, ge=1, description="Maximum number of projects to return")
):
    """Fetch the list of projects with optional filtering and pagination"""
    filtered_projects = [project for project in projects if name is None or name.lower() in project["name"].lower()]
    return filtered_projects[skip: skip + limit]

@router.post("/projects", response_model=dict)
async def create_project(project: dict):
    """Create a new project"""
    new_id = max(project["id"] for project in projects) + 1 if projects else 1
    project["id"] = new_id
    projects.append(project)
    return project

@router.get("/projects/{project_id}", response_model=dict)
async def get_project(project_id: int):
    """Fetch a single project by ID"""
    project = next((project for project in projects if project["id"] == project_id), None)
    if project is None:
        return {"error": "Project not found"}
    return project

@router.put("/projects/{project_id}", response_model=dict)
async def update_project(project_id: int, updated_project: dict):
    """Update an existing project"""
    for project in projects:
        if project["id"] == project_id:
            project.update(updated_project)
            return project
    return {"error": "Project not found"}

@router.delete("/projects/{project_id}", response_model=dict)
async def delete_project(project_id: int):
    """Delete a project by ID"""
    global projects
    projects = [project for project in projects if project["id"] != project_id]
    return {"message": "Project deleted"}
