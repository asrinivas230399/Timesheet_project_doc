from billing_management import BillingManager

class ProjectsList:
    def __init__(self, billing_manager):
        self.billing_manager = billing_manager
        self.projects = []  # List to store project details

    def add_project(self, project_id, project_currency, hourly_rate):
        """Add a project to the list with its currency and hourly rate."""
        project_details = {
            'id': project_id,
            'currency': project_currency,
            'hourly_rate': hourly_rate
        }
        self.projects.append(project_details)

    def list_projects(self):
        """Display all projects with their currency and hourly rates."""
        print("Projects List:")
        for project in self.projects:
            print(f"Project ID: {project['id']}, Currency: {project['currency']}, Hourly Rate: {project['hourly_rate']}")

    def display_project_details(self, project_id):
        """Display detailed information for a specific project by ID."""
        project = next((proj for proj in self.projects if proj['id'] == project_id), None)
        if project:
            print(f"Project ID: {project['id']}")
            print(f"Currency: {project['currency']}")
            print(f"Hourly Rate: {project['hourly_rate']}")
        else:
            print(f"Project with ID {project_id} not found.")

# Example usage
if __name__ == "__main__":
    billing_manager = BillingManager()
    billing_manager.set_currency('USD')
    projects_list = ProjectsList(billing_manager)
    projects_list.add_project(1, 'USD', 100)
    projects_list.add_project(2, 'EUR', 150)
    projects_list.list_projects()  # Display the list of projects with their details
    projects_list.display_project_details(1)  # Display details for project with ID 1
    projects_list.display_project_details(3)  # Attempt to display details for a non-existent project