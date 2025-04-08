import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LoggingService:
    @staticmethod
    def log_access_attempt(username, success):
        """Log an access attempt by a user."""
        if success:
            logging.info(f"Access attempt successful for user: {username}")
        else:
            logging.warning(f"Access attempt failed for user: {username}")

    @staticmethod
    def log_user_action(user_id, action):
        """Log an action performed by a user."""
        logging.info(f"User {user_id} performed action: {action}")

    @staticmethod
    def log_role_change(role_id, change_description):
        """Log changes to roles or permissions."""
        logging.info(f"Role {role_id} changed: {change_description}")
