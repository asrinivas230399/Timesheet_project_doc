class CustomerDataSynchronization:
    def __init__(self, connection_manager):
        self.connection_manager = connection_manager
        self.is_synchronized = False

    def start_customer_data_synchronization(self):
        """
        Starts the customer data synchronization process if the connection is active.
        This is a placeholder for actual synchronization logic.
        """
        if self.connection_manager.connection is not None:
            if not self.is_synchronized:
                # Placeholder for starting customer data synchronization logic
                self.is_synchronized = True
                print("Customer data synchronization started.")
            else:
                print("Customer data synchronization already in progress.")
        else:
            print("Cannot start customer data synchronization. No active connection.")

    def stop_customer_data_synchronization(self):
        """
        Stops the customer data synchronization process.
        This is a placeholder for actual stop synchronization logic.
        """
        if self.is_synchronized:
            # Placeholder for stopping customer data synchronization logic
            self.is_synchronized = False
            print("Customer data synchronization stopped.")
        else:
            print("No customer data synchronization process to stop.")

    def synchronize_customer_data_now(self):
        """
        Performs an immediate customer data synchronization if the connection is active.
        This is a placeholder for actual immediate synchronization logic.
        """
        if self.connection_manager.connection is not None:
            if self.is_synchronized:
                # Placeholder for immediate customer data synchronization logic
                print("Immediate customer data synchronization performed.")
            else:
                print("Cannot perform immediate customer data synchronization. Synchronization is not active.")
        else:
            print("Cannot perform immediate customer data synchronization. No active connection.")