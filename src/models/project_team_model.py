from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

# Association table for many-to-many relationship between Project and TeamMember
project_team_member_association = Table(
    'project_team_member', Base.metadata,
    Column('project_id', Integer, ForeignKey('projects.id')),
    Column('team_member_id', Integer, ForeignKey('team_members.id'))
)

class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    team_members = relationship('TeamMember', secondary=project_team_member_association, back_populates='projects')

class TeamMember(Base):
    __tablename__ = 'team_members'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    projects = relationship('Project', secondary=project_team_member_association, back_populates='team_members')