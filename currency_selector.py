from billing_management import BillingManager

class CurrencySelector:
    def __init__(self, default_currencies=None):
        if default_currencies is None:
            default_currencies = self.get_currency_list()
        self.available_currencies = default_currencies
        self.selected_currency = default_currencies[0]  # Default to the first currency
        self.billing_manager = BillingManager()

    def add_currency(self, currency):
        """Add a new currency to the list of available currencies."""
        if currency not in self.available_currencies:
            self.available_currencies.append(currency)
        else:
            print(f"{currency} is already in the list of available currencies.")

    def remove_currency(self, currency):
        """Remove a currency from the list of available currencies."""
        if currency in self.available_currencies:
            self.available_currencies.remove(currency)
        else:
            print(f"{currency} is not in the list of available currencies.")

    def select_currency(self, currency_code):
        """Validate and set the selected currency from the available currencies."""
        if currency_code in self.available_currencies:
            self.selected_currency = currency_code
            self.billing_manager.set_currency(currency_code)
            print(f"Selected currency set to {currency_code}.")
        else:
            print(f"{currency_code} is not available for selection.")

    def confirm_currency_selection(self):
        """Return a confirmation message upon successful currency selection."""
        return f"Currency {self.selected_currency} has been successfully selected."

    def get_selected_currency(self):
        """Return the currently selected currency."""
        return self.selected_currency

    def list_currencies(self):
        """Return the list of available currencies."""
        return self.available_currencies

    def get_currency_list(self):
        """Fetch the list of currencies from a configuration file."""
        try:
            with open('config/currencies.txt', 'r') as file:
                currencies = file.read().splitlines()
            return currencies
        except FileNotFoundError:
            print("Configuration file not found. Using default currencies.")
            return ['USD', 'EUR', 'GBP']

    def display_currency_selection(self):
        """Display the currency selection interface to the user."""
        print("Available currencies:")
        for currency in self.available_currencies:
            print(f"- {currency}")
        print(f"Currently selected currency: {self.selected_currency}")