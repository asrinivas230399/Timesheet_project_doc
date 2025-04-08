from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel

# Define a simple Project model for demonstration purposes
class Project(BaseModel):
    id: int
    name: str
    description: str

# Create a router object
router = APIRouter()

# In-memory "database" for demonstration
projects_db = [
    Project(id=1, name="Project Alpha", description="Description of Project Alpha"),
    Project(id=2, name="Project Beta", description="Description of Project Beta"),
]

@router.get("/projects", response_model=List[Project])
async def get_projects():
    """
    Get the list of projects.
    """
    return projects_db

@router.post("/projects", response_model=Project)
async def add_project(project: Project):
    """
    Add a new project.
    """
    projects_db.append(project)
    return project

@router.put("/projects/{project_id}", response_model=Project)
async def edit_project(project_id: int, updated_project: Project):
    """
    Edit an existing project.
    """
    for index, project in enumerate(projects_db):
        if project.id == project_id:
            projects_db[index] = updated_project
            return updated_project
    raise HTTPException(status_code=404, detail="Project not found")
