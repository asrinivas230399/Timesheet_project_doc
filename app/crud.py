from sqlalchemy.orm import Session
from app import models


def get_project(db: Session):
    return db.query(models.Project).first()


def update_task_status(db: Session, task_id: int, status: str):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task:
        task.status = status
        db.commit()
        db.refresh(task)
    return task


def get_tasks(db: Session):
    return db.query(models.Task).all()