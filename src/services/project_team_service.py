from src.repositories.project_team_repository import ProjectTeamRepository

project_team_repository = ProjectTeamRepository()

def assign_project_team(project_id: int, team_member_ids: list):
    try:
        # Check if project exists
        if not project_team_repository.project_exists(project_id):
            raise ValueError("Project does not exist")

        # Assign team members to the project
        project_team_repository.assign_team_members(project_id, team_member_ids)

        return {"message": "Team members assigned successfully", "project_id": project_id, "team_member_ids": team_member_ids}
    except Exception as e:
        raise e

def edit_project_team(project_id: int, team_member_ids: list):
    try:
        # Check if project exists
        if not project_team_repository.project_exists(project_id):
            raise ValueError("Project does not exist")

        # Update team members for the project
        project_team_repository.update_team_members(project_id, team_member_ids)

        return {"message": "Team members updated successfully", "project_id": project_id, "team_member_ids": team_member_ids}
    except Exception as e:
        raise e