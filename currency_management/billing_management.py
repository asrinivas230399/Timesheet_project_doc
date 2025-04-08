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

    def apply_currency_to_billing(self, currency_code):
        """Apply the selected currency in billing calculations."""
        print(f"Applying {currency_code} to billing calculations.")

    def validate_billing_currency(self, project_currency):
        """Ensure billing currency matches the selected project currency."""
        if self.current_currency == project_currency:
            print("Billing currency matches the selected project currency.")
            return True
        else:
            print("Billing currency does not match the selected project currency.")
            return False