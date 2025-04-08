from billing_management import BillingManager

class ProjectAdd:
    def __init__(self, billing_manager):
        self.billing_manager = billing_manager

    def add_project(self, project_currency):
        """Add a new project with the specified currency."""
        if self.billing_manager.validate_billing_currency(project_currency):
            print(f"Project added with currency: {project_currency}")
        else:
            print("Failed to add project due to currency mismatch.")