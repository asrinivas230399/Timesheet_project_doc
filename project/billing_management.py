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