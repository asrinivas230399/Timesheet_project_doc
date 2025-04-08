from sqlalchemy.orm import Session
from src.models import Project, TeamMember

class ProjectTeamRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def project_exists(self, project_id: int) -> bool:
        # Check if the project exists in the database
        return self.db_session.query(Project).filter(Project.id == project_id).first() is not None

    def assign_team_members(self, project_id: int, team_member_ids: list):
        # Assign team members to a project in the database
        project = self.db_session.query(Project).filter(Project.id == project_id).first()
        if project:
            team_members = self.db_session.query(TeamMember).filter(TeamMember.id.in_(team_member_ids)).all()
            project.team_members = team_members
            self.db_session.commit()

    def update_team_members(self, project_id: int, team_member_ids: list):
        # Update team members of a project in the database
        project = self.db_session.query(Project).filter(Project.id == project_id).first()
        if project:
            team_members = self.db_session.query(TeamMember).filter(TeamMember.id.in_(team_member_ids)).all()
            project.team_members = team_members
            self.db_session.commit()