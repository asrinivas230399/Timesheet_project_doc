class AuditService:
    def __init__(self):
        self.audit_log = []

    def log_activity(self, user_id: str, activity: str):
        """
        Logs a user activity for audit purposes.
        """
        event = f"User {user_id}: {activity}"
        self.audit_log.append(event)
        print(f"Audit log: {event}")

    def get_audit_log(self) -> list:
        """
        Retrieves the audit log.
        """
        return self.audit_log
