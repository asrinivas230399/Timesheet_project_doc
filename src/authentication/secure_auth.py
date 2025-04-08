import hashlib
import pyotp
import os

class SecureAuth:
    def __init__(self):
        # This would typically be stored securely in a database
        self.users = {}

    def hash_password(self, password: str) -> str:
        """Hash a password for storing."""
        salt = os.urandom(16)
        pwdhash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        return salt + pwdhash

    def verify_password(self, stored_password: bytes, provided_password: str) -> bool:
        """Verify a stored password against one provided by user"""
        salt = stored_password[:16]
        stored_pwdhash = stored_password[16:]
        pwdhash = hashlib.pbkdf2_hmac('sha256', provided_password.encode('utf-8'), salt, 100000)
        return pwdhash == stored_pwdhash

    def register_user(self, username: str, password: str):
        """Register a new user with a username and password."""
        if username in self.users:
            raise Exception("User already exists")
        self.users[username] = {
            'password': self.hash_password(password),
            'totp_secret': pyotp.random_base32()
        }
        print(f"User {username} registered successfully.")

    def authenticate_user(self, username: str, password: str) -> bool:
        """Authenticate user with username and password."""
        if username not in self.users:
            return False
        stored_password = self.users[username]['password']
        return self.verify_password(stored_password, password)

    def generate_mfa_token(self, username: str) -> str:
        """Generate a TOTP token for the user."""
        if username not in self.users:
            raise Exception("User not found")
        totp_secret = self.users[username]['totp_secret']
        totp = pyotp.TOTP(totp_secret)
        return totp.now()

    def verify_mfa_token(self, username: str, token: str) -> bool:
        """Verify the provided TOTP token."""
        if username not in self.users:
            return False
        totp_secret = self.users[username]['totp_secret']
        totp = pyotp.TOTP(totp_secret)
        return totp.verify(token)

# Example usage
if __name__ == "__main__":
    auth = SecureAuth()
    auth.register_user("john_doe", "securepassword123")
    print("Authentication:", auth.authenticate_user("john_doe", "securepassword123"))
    token = auth.generate_mfa_token("john_doe")
    print("MFA Token:", token)
    print("MFA Verification:", auth.verify_mfa_token("john_doe", token))