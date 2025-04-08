from pydantic import BaseModel

# Define a simple Project model for demonstration purposes
class Project(BaseModel):
    id: int
    name: str
    description: str
