from src.role_management.rbac import RBAC

class RoleAssignment:
    def __init__(self, rbac: RBAC):
        self.rbac = rbac

    def assign_role(self, username: str, role_name: str):
        """Assign a role to a user, ensuring compliance with defined permissions."""
        if role_name not in self.rbac.roles:
            raise Exception("Role does not exist")
        if username not in self.rbac.users:
            self.rbac.users[username] = User(username)
        self.rbac.assign_role_to_user(username, role_name)

    def modify_role(self, username: str, old_role_name: str, new_role_name: str):
        """Modify a user's role, ensuring compliance with defined permissions."""
        if old_role_name not in self.rbac.roles or new_role_name not in self.rbac.roles:
            raise Exception("Role does not exist")
        user = self.rbac.users.get(username)
        if not user:
            raise Exception("User does not exist")
        old_role = self.rbac.roles[old_role_name]
        new_role = self.rbac.roles[new_role_name]
        user.remove_role(old_role)
        user.add_role(new_role)

    def get_user_roles(self, username: str) -> list:
        """Retrieve all roles assigned to a user."""
        user = self.rbac.users.get(username)
        if not user:
            raise Exception("User does not exist")
        return [role.name for role in user.roles]