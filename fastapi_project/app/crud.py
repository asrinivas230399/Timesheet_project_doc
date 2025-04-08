from sqlalchemy.orm import Session
from app import models

def get_project(db: Session):
    return db.query(models.Project).first()
