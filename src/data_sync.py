import threading
import time
from src.crm_integration import CRMIntegration
from src.logging.sync_logging import SyncLogging

class DataSync:
    def __init__(self, crm_integration: CRMIntegration, sync_interval: int = 60):
        self.crm_integration = crm_integration
        self.sync_interval = sync_interval
        self.sync_thread = threading.Thread(target=self.run_sync, daemon=True)
        self.sync_logging = SyncLogging()

    def start_sync(self):
        """Start the synchronization process in a separate thread."""
        self.sync_thread.start()

    def run_sync(self):
        """Run the synchronization process at regular intervals."""
        while True:
            try:
                self.sync_logging.log_sync_event("Starting data synchronization...")
                self.crm_integration.synchronize_customers()
                self.sync_logging.log_sync_event("Data synchronization completed.")
            except Exception as e:
                self.sync_logging.log_sync_event(f"Error during synchronization: {e}")
            time.sleep(self.sync_interval)

# Example usage
if __name__ == "__main__":
    crm_integration = CRMIntegration(api_url="https://api.example-crm.com", api_key="your_api_key_here")
    data_sync = DataSync(crm_integration)
    data_sync.start_sync()
    
    # Simulate main application running
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping data synchronization...")
