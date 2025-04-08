class Billing:
    def __init__(self, rate_per_hour=None, fixed_rate=None):
        self.rate_per_hour = rate_per_hour
        self.fixed_rate = fixed_rate

    def calculate_fixed_rate_billing(self):
        """
        Calculates the billing amount for a fixed rate project.
        """
        if self.fixed_rate is not None:
            return self.fixed_rate
        else:
            raise ValueError("Fixed rate is not set.")

    def calculate_time_and_material_billing(self, hours_worked):
        """
        Calculates the billing amount for a time and material project.
        """
        if self.rate_per_hour is not None:
            return self.rate_per_hour * hours_worked
        else:
            raise ValueError("Rate per hour is not set.")

    def format_billing_data(self, billing_amount, project_type):
        """
        Formats the billing data for integration with financial systems.
        """
        return {
            "project_type": project_type,
            "billing_amount": billing_amount,
            "currency": "USD",  # Assuming USD for simplicity
            "status": "Pending"
        }