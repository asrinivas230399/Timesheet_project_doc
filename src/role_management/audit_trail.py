import datetime

class AuditTrail:
    def __init__(self):
        self.logs = []

    def log_role_assignment(self, username: str, role_name: str, changed_by: str):
        timestamp = datetime.datetime.now()
        log_entry = f"{timestamp}: User '{changed_by}' assigned role '{role_name}' to user '{username}'."
        self.logs.append(log_entry)
        print(log_entry)

    def log_role_modification(self, username: str, old_role_name: str, new_role_name: str, changed_by: str):
        timestamp = datetime.datetime.now()
        log_entry = f"{timestamp}: User '{changed_by}' modified role for user '{username}' from '{old_role_name}' to '{new_role_name}'."
        self.logs.append(log_entry)
        print(log_entry)

    def get_logs(self) -> list:
        return self.logs