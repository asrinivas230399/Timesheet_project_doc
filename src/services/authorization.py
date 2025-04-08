from models.user import User
from models.role import Role

class AuthorizationService:
    @staticmethod
    def user_has_permission(user_id, permission):
        """Check if the user has a specific permission based on their role."""
        user = User.find_by_id(user_id)
        if not user:
            return False

        role = Role.find_by_id(user.role)
        if not role:
            return False

        return permission in role.permissions

    @staticmethod
    def get_user_permissions(user_id):
        """Get all permissions for a user based on their role."""
        user = User.find_by_id(user_id)
        if not user:
            return []

        role = Role.find_by_id(user.role)
        if not role:
            return []

        return role.permissions