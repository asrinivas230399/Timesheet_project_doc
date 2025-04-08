import json
import time

class ProjectUpdates:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, client_callback):
        """
        Subscribe a client to receive updates.
        :param client_callback: A callback function to push updates to the client.
        """
        self.subscribers.append(client_callback)

    def unsubscribe(self, client_callback):
        """
        Unsubscribe a client from receiving updates.
        :param client_callback: The callback function to remove.
        """
        self.subscribers.remove(client_callback)

    def notify_subscribers(self, update):
        """
        Notify all subscribers with the latest update.
        :param update: The update data to send to subscribers.
        """
        for subscriber in self.subscribers:
            subscriber(update)

    def push_update(self, update_data):
        """
        Push a new update to all subscribers.
        :param update_data: The data to be sent as an update.
        """
        update = json.dumps(update_data)
        self.notify_subscribers(update)

    def simulate_updates(self):
        """
        Simulate real-time updates for demonstration purposes.
        """
        for i in range(5):
            update_data = {
                'update_id': i,
                'timestamp': time.time(),
                'message': f'Update {i} received'
            }
            self.push_update(update_data)
            time.sleep(1)  # Simulate delay between updates
