from sqlalchemy.orm import Session
from src.models import Project

class ProjectListRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_all_projects(self):
        # Fetch all projects from the database
        return self.db_session.query(Project).all()

    def get_project_by_id(self, project_id: int):
        # Fetch a single project by its ID
        return self.db_session.query(Project).filter(Project.id == project_id).first()