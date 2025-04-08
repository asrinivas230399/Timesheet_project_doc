from billing_management import BillingManager
from currency_selection import CurrencySelector

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

# Example usage
if __name__ == "__main__":
    currency_selector = CurrencySelector()
    currency_selector.select_currency('USD')
    project_add = ProjectAdd(currency_selector.billing_manager)
    project_add.add_project('USD', 100)  # Example project with USD currency and hourly rate of 100