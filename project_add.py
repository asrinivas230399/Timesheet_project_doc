from billing_management import BillingManager

class ProjectAdd:
    def __init__(self, billing_manager):
        self.billing_manager = billing_manager

    def add_project(self, project_currency, hourly_rate):
        """Add a new project with the specified currency and hourly rate."""
        if self.billing_manager.validate_billing_currency(project_currency):
            self.billing_manager.set_hourly_rate(hourly_rate)
            print(f"Project added with currency: {project_currency} and hourly rate: {hourly_rate}")
        else:
            print("Failed to add project due to currency mismatch.")