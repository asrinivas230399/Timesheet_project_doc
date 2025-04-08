from pydantic import BaseModel, Field
from typing import Optional

class ProjectSchema(BaseModel):
    id: int = Field(..., description="The ID of the project")
    name: str = Field(..., description="The name of the project")

class ProjectListResponseSchema(BaseModel):
    projects: list[ProjectSchema] = Field(..., description="List of projects")

class ProjectDetailSchema(BaseModel):
    id: int = Field(..., description="The ID of the project")
    name: str = Field(..., description="The name of the project")
    team_member_ids: Optional[list[int]] = Field(None, description="List of team member IDs associated with the project")