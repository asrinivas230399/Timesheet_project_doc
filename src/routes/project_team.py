from fastapi import APIRouter, HTTPException
from src.schemas.project_team_schema import AssignProjectTeamSchema, EditProjectTeamSchema
from src.services.project_team_service import assign_project_team, edit_project_team

router = APIRouter()

@router.post("/assign-team")
async def assign_team(request: AssignProjectTeamSchema):
    try:
        result = assign_project_team(request.project_id, request.team_member_ids)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/edit-team")
async def edit_team(request: EditProjectTeamSchema):
    try:
        result = edit_project_team(request.project_id, request.team_member_ids)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))