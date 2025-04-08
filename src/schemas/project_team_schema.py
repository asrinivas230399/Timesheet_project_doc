from pydantic import BaseModel, Field
from typing import List

class AssignProjectTeamSchema(BaseModel):
    project_id: int = Field(..., description="The ID of the project")
    team_member_ids: List[int] = Field(..., description="List of team member IDs to be assigned to the project")

class EditProjectTeamSchema(BaseModel):
    project_id: int = Field(..., description="The ID of the project")
    team_member_ids: List[int] = Field(..., description="Updated list of team member IDs for the project")