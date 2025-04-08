from src.repositories.project_repository import ProjectRepository

def get_project_list():
    try:
        # Initialize the repository
        project_repository = ProjectRepository()
        
        # Retrieve the list of projects
        projects = project_repository.get_all_projects()
        
        # Return the list of projects
        return projects
    except Exception as e:
        raise e