import json

class UserInterface:
    def __init__(self, project_view, project_updates):
        self.project_view = project_view
        self.project_updates = project_updates

    def display_menu(self):
        print("Welcome to the Project Management System")
        print("1. View Project Information")
        print("2. Subscribe to Project Updates")
        print("3. Unsubscribe from Project Updates")
        print("4. Exit")

    def handle_user_input(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.view_project_info()
            elif choice == '2':
                self.subscribe_to_updates()
            elif choice == '3':
                self.unsubscribe_from_updates()
            elif choice == '4':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

    def view_project_info(self):
        project_id = input("Enter the project ID: ")
        project_info = self.project_view.get_project_info(project_id)
        if project_info:
            print(json.dumps(project_info, indent=4))
        else:
            print(f"Project with ID {project_id} not found.")

    def subscribe_to_updates(self):
        def update_callback(update):
            print("Received update:", update)
        self.project_updates.subscribe(update_callback)
        print("Subscribed to project updates.")

    def unsubscribe_from_updates(self):
        def update_callback(update):
            pass  # Placeholder for the callback to be removed
        self.project_updates.unsubscribe(update_callback)
        print("Unsubscribed from project updates.")
