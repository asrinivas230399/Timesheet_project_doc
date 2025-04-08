from cryptography.fernet import Fernet

class EncryptionService:
    def __init__(self, key: bytes):
        self.cipher = Fernet(key)

    def encrypt(self, data: str) -> bytes:
        """
        Encrypts the given data using Fernet symmetric encryption.
        """
        return self.cipher.encrypt(data.encode())

    def decrypt(self, token: bytes) -> str:
        """
        Decrypts the given token back to the original data.
        """
        return self.cipher.decrypt(token).decode()

    @staticmethod
    def generate_key() -> bytes:
        """
        Generates a new Fernet key for encryption and decryption.
        """
        return Fernet.generate_key()