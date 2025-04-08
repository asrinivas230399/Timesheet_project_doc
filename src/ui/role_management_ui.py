from src.role_management.rbac import RBAC
from src.role_management.role_assignment import RoleAssignment
from src.audit_trail import AuditTrail

class RoleManagementUI:
    def __init__(self, rbac: RBAC, role_assignment: RoleAssignment, audit_trail: AuditTrail):
        self.rbac = rbac
        self.role_assignment = role_assignment
        self.audit_trail = audit_trail

    def display_menu(self):
        print("Role Management System")
        print("1. Create Role")
        print("2. Assign Role to User")
        print("3. Modify User Role")
        print("4. View User Roles")
        print("5. View Audit Logs")
        print("6. Exit")

    def create_role(self):
        role_name = input("Enter role name: ")
        try:
            self.rbac.create_role(role_name)
            print(f"Role '{role_name}' created successfully.")
        except Exception as e:
            print(e)

    def assign_role_to_user(self):
        username = input("Enter username: ")
        role_name = input("Enter role name: ")
        changed_by = input("Enter your username: ")
        try:
            self.role_assignment.assign_role(username, role_name)
            self.audit_trail.log_role_assignment(username, role_name, changed_by)
            print(f"Role '{role_name}' assigned to user '{username}' successfully.")
        except Exception as e:
            print(e)

    def modify_user_role(self):
        username = input("Enter username: ")
        old_role_name = input("Enter old role name: ")
        new_role_name = input("Enter new role name: ")
        changed_by = input("Enter your username: ")
        try:
            self.role_assignment.modify_role(username, old_role_name, new_role_name)
            self.audit_trail.log_role_modification(username, old_role_name, new_role_name, changed_by)
            print(f"User '{username}' role changed from '{old_role_name}' to '{new_role_name}' successfully.")
        except Exception as e:
            print(e)

    def view_user_roles(self):
        username = input("Enter username: ")
        try:
            roles = self.role_assignment.get_user_roles(username)
            print(f"User '{username}' has roles: {', '.join(roles)}")
        except Exception as e:
            print(e)

    def view_audit_logs(self):
        logs = self.audit_trail.get_logs()
        print("Audit Logs:")
        for log in logs:
            print(log)

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.create_role()
            elif choice == '2':
                self.assign_role_to_user()
            elif choice == '3':
                self.modify_user_role()
            elif choice == '4':
                self.view_user_roles()
            elif choice == '5':
                self.view_audit_logs()
            elif choice == '6':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

# Example usage
if __name__ == "__main__":
    rbac = RBAC()
    role_assignment = RoleAssignment(rbac)
    audit_trail = AuditTrail()
    ui = RoleManagementUI(rbac, role_assignment, audit_trail)
    ui.run()