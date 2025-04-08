from sqlalchemy.orm import Session
from .project import Project


def get_project_by_id(db: Session, project_id: int) -> Project:
    """Fetch a single project by ID from the database"""
    return db.query(Project).filter(Project.id == project_id).first()


def get_projects(db: Session, skip: int = 0, limit: int = 10) -> list[Project]:
    """Fetch a list of projects with pagination"""
    return db.query(Project).offset(skip).limit(limit).all()


def create_project(db: Session, project: Project) -> Project:
    """Create a new project in the database"""
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


def update_project(db: Session, project_id: int, updated_data: dict) -> Project:
    """Update an existing project in the database"""
    project = get_project_by_id(db, project_id)
    if project:
        for key, value in updated_data.items():
            setattr(project, key, value)
        db.commit()
        db.refresh(project)
    return project


def delete_project(db: Session, project_id: int) -> bool:
    """Delete a project by ID from the database"""
    project = get_project_by_id(db, project_id)
    if project:
        db.delete(project)
        db.commit()
        return True
    return False
