from fastapi import APIRouter, HTTPException
from src.services.project_service import get_project_list

router = APIRouter()

@router.get("/projects")
async def list_projects():
    try:
        projects = get_project_list()
        return projects
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))