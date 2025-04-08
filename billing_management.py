class BillingManager:
    def __init__(self):
        self.current_currency = None

    def set_currency(self, currency):
        """Set the currency for billing."""
        self.current_currency = currency
        print(f"Billing currency set to {currency}.")

    def get_currency(self):
        """Get the current billing currency."""
        return self.current_currency

    def validate_billing_currency(self, project_currency):
        """Ensure billing currency matches the selected project currency."""
        if self.current_currency == project_currency:
            print("Billing currency matches the selected project currency.")
            return True
        else:
            print("Billing currency does not match the selected project currency.")
            return False