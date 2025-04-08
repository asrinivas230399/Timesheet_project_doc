import logging
import time

# Configure logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

class ErrorHandling:
    def __init__(self, max_retries=3, retry_delay=5):
        self.max_retries = max_retries
        self.retry_delay = retry_delay

    def log_error(self, error_message):
        """
        Logs an error message.
        """
        logging.error(error_message)

    def notify_user(self, notification_message):
        """
        Notifies the user about an error or important information.
        This is a placeholder for actual user notification logic.
        """
        print(f"Notification: {notification_message}")

    def retry_operation(self, operation, *args, **kwargs):
        """
        Retries a given operation if it fails, up to a maximum number of retries.
        """
        attempt = 0
        while attempt < self.max_retries:
            try:
                return operation(*args, **kwargs)
            except Exception as e:
                self.log_error(f"Error occurred: {e}. Retrying {attempt + 1}/{self.max_retries}...")
                self.notify_user(f"An error occurred: {e}. Retrying...")
                attempt += 1
                time.sleep(self.retry_delay)
        self.notify_user("Operation failed after multiple attempts.")
        raise Exception("Operation failed after maximum retries.")