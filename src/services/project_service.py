from typing import List
from pydantic import BaseModel

# Define a simple Project model for demonstration purposes
class Project(BaseModel):
    id: int
    name: str
    description: str

# In-memory "database" for demonstration
projects_db = [
    Project(id=1, name="Project Alpha", description="Description of Project Alpha"),
    Project(id=2, name="Project Beta", description="Description of Project Beta"),
]

def get_projects() -> List[Project]:
    """
    Get the list of projects.
    """
    return projects_db


def add_project(project: Project) -> Project:
    """
    Add a new project.
    """
    projects_db.append(project)
    return project


def edit_project(project_id: int, updated_project: Project) -> Project:
    """
    Edit an existing project.
    """
    for index, project in enumerate(projects_db):
        if project.id == project_id:
            projects_db[index] = updated_project
            return updated_project
    raise ValueError("Project not found")