from models.user import User
import uuid

class AuthenticationService:
    _sessions = {}

    @staticmethod
    def login(username, password):
        """Authenticate user and create a session token."""
        user = User.find_by_username(username)
        if user and user.password == password:
            # Create a session token
            session_token = str(uuid.uuid4())
            AuthenticationService._sessions[session_token] = user.user_id
            return session_token
        return None

    @staticmethod
    def logout(session_token):
        """Logout user by removing the session token."""
        if session_token in AuthenticationService._sessions:
            del AuthenticationService._sessions[session_token]
            return True
        return False

    @staticmethod
    def is_authenticated(session_token):
        """Check if the session token is valid."""
        return session_token in AuthenticationService._sessions

    @staticmethod
    def get_user_id_from_session(session_token):
        """Get user_id from session token."""
        return AuthenticationService._sessions.get(session_token)