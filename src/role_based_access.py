class RoleBasedAccessControl:
    def __init__(self):
        # Define roles and their permissions
        self.roles_permissions = {
            'admin': {'read', 'write', 'delete'},
            'editor': {'read', 'write'},
            'viewer': {'read'}
        }
        # User roles mapping
        self.user_roles = {}

    def assign_role(self, username, role):
        # Assign a role to a user
        if role not in self.roles_permissions:
            raise ValueError(f"Role '{role}' does not exist")
        self.user_roles[username] = role

    def check_permission(self, username, permission):
        # Check if a user has a specific permission
        role = self.user_roles.get(username)
        if not role:
            raise ValueError(f"User '{username}' does not have an assigned role")
        return permission in self.roles_permissions[role]

    def get_user_role(self, username):
        # Get the role of a user
        return self.user_roles.get(username)