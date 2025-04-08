import datetime

class SyncLogging:
    def __init__(self):
        self.logs = []

    def log_sync_event(self, message: str):
        timestamp = datetime.datetime.now()
        log_entry = f"{timestamp}: {message}"
        self.logs.append(log_entry)
        print(log_entry)

    def get_logs(self) -> list:
        return self.logs
