from billing_management import BillingManager
from currency_selection import CurrencySelector

class ProjectEdit:
    def __init__(self, billing_manager):
        self.billing_manager = billing_manager

    def edit_project(self, project_id, project_currency, new_hourly_rate):
        """Edit an existing project with the specified currency and new hourly rate."""
        if self.billing_manager.validate_billing_currency(project_currency):
            self.billing_manager.modify_hourly_rate(new_hourly_rate)
            print(f"Project {project_id} edited with currency: {project_currency} and new hourly rate: {new_hourly_rate}")
        else:
            print("Failed to edit project due to currency mismatch.")

# Example usage
if __name__ == "__main__":
    currency_selector = CurrencySelector()
    currency_selector.select_currency('USD')
    project_edit = ProjectEdit(currency_selector.billing_manager)
    project_edit.edit_project(1, 'USD', 120)  # Example project edit with USD currency and new hourly rate of 120