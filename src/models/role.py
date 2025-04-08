class Role:
    def __init__(self, role_id, role_name, permissions):
        self.role_id = role_id
        self.role_name = role_name
        self.permissions = permissions

    # In-memory database simulation
    _role_db = {}

    def save_to_db(self):
        """Save the role to the in-memory database."""
        Role._role_db[self.role_id] = self

    @classmethod
    def find_by_role_name(cls, role_name):
        """Find a role by role_name."""
        for role in cls._role_db.values():
            if role.role_name == role_name:
                return role
        return None

    @classmethod
    def find_by_id(cls, role_id):
        """Find a role by role_id."""
        return cls._role_db.get(role_id, None)