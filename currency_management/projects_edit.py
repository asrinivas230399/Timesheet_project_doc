from billing_management import BillingManager

class ProjectEdit:
    def __init__(self, billing_manager):
        self.billing_manager = billing_manager

    def edit_project(self, project_currency):
        """Edit an existing project with the specified currency."""
        if self.billing_manager.validate_billing_currency(project_currency):
            print(f"Project edited with currency: {project_currency}")
        else:
            print("Failed to edit project due to currency mismatch.")