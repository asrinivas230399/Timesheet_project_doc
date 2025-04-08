from typing import List, Optional

# In-memory project list for demonstration purposes
projects = [
    {"id": 1, "name": "Project Alpha"},
    {"id": 2, "name": "Project Beta"}
]

async def get_projects(name: Optional[str] = None, skip: int = 0, limit: int = 10) -> List[dict]:
    """Fetch the list of projects with optional filtering and pagination"""
    # Apply business logic for filtering
    filtered_projects = [project for project in projects if name is None or name.lower() in project["name"].lower()]
    # Apply business logic for pagination
    paginated_projects = filtered_projects[skip: skip + limit]
    return paginated_projects

async def create_project(project: dict) -> dict:
    """Create a new project"""
    new_id = max(project["id"] for project in projects) + 1 if projects else 1
    project["id"] = new_id
    projects.append(project)
    return project

async def get_project(project_id: int) -> dict:
    """Fetch a single project by ID"""
    project = next((project for project in projects if project["id"] == project_id), None)
    if project is None:
        return {"error": "Project not found"}
    return project

async def update_project(project_id: int, updated_project: dict) -> dict:
    """Update an existing project"""
    for project in projects:
        if project["id"] == project_id:
            project.update(updated_project)
            return project
    return {"error": "Project not found"}

async def delete_project(project_id: int) -> dict:
    """Delete a project by ID"""
    global projects
    projects = [project for project in projects if project["id"] != project_id]
    return {"message": "Project deleted"}