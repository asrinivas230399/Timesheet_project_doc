class User:
    def __init__(self, user_id, username, password, role):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.role = role

    # In-memory database simulation
    _user_db = {}

    def save_to_db(self):
        """Save the user to the in-memory database."""
        User._user_db[self.user_id] = self

    @classmethod
    def find_by_username(cls, username):
        """Find a user by username."""
        for user in cls._user_db.values():
            if user.username == username:
                return user
        return None

    @classmethod
    def find_by_id(cls, user_id):
        """Find a user by user_id."""
        return cls._user_db.get(user_id, None)