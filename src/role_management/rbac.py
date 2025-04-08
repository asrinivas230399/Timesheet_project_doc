from src.role_management.role import Role
from src.role_management.user import User

class RBAC:
    def __init__(self):
        self.roles = {}
        self.users = {}

    def create_role(self, role_name: str):
        if role_name in self.roles:
            raise Exception("Role already exists")
        self.roles[role_name] = Role(role_name)

    def assign_role_to_user(self, username: str, role_name: str):
        if username not in self.users:
            self.users[username] = User(username)
        if role_name not in self.roles:
            raise Exception("Role does not exist")
        self.users[username].add_role(self.roles[role_name])

    def user_has_permission(self, username: str, permission: str) -> bool:
        if username not in self.users:
            return False
        return self.users[username].has_permission(permission)

    def add_permission_to_role(self, role_name: str, permission: str):
        if role_name not in self.roles:
            raise Exception("Role does not exist")
        self.roles[role_name].add_permission(permission)

    def remove_permission_from_role(self, role_name: str, permission: str):
        if role_name not in self.roles:
            raise Exception("Role does not exist")
        self.roles[role_name].remove_permission(permission)