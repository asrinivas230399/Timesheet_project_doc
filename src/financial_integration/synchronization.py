class DataSynchronization:
    def __init__(self, connection_manager):
        self.is_synchronized = False
        self.connection_manager = connection_manager

    def start_synchronization(self):
        """
        Starts the real-time data synchronization process if the connection is active.
        This is a placeholder for actual synchronization logic.
        """
        if self.connection_manager.connection is not None:
            if not self.is_synchronized:
                # Placeholder for starting synchronization logic
                self.is_synchronized = True
                print("Data synchronization started.")
            else:
                print("Data synchronization already in progress.")
        else:
            print("Cannot start synchronization. No active connection.")

    def stop_synchronization(self):
        """
        Stops the real-time data synchronization process.
        This is a placeholder for actual stop synchronization logic.
        """
        if self.is_synchronized:
            # Placeholder for stopping synchronization logic
            self.is_synchronized = False
            print("Data synchronization stopped.")
        else:
            print("No synchronization process to stop.")

    def synchronize_now(self):
        """
        Performs an immediate synchronization if the connection is active.
        This is a placeholder for actual immediate synchronization logic.
        """
        if self.connection_manager.connection is not None:
            if self.is_synchronized:
                # Placeholder for immediate synchronization logic
                print("Immediate data synchronization performed.")
            else:
                print("Cannot perform immediate synchronization. Synchronization is not active.")
        else:
            print("Cannot perform immediate synchronization. No active connection.")