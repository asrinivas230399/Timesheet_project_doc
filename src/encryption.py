from cryptography.fernet import Fernet

class DataEncryption:
    def __init__(self, key=None):
        # Generate a new key if none is provided
        self.key = key or Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt_data(self, data):
        # Encrypt the data
        if isinstance(data, str):
            data = data.encode('utf-8')
        encrypted_data = self.cipher.encrypt(data)
        return encrypted_data

    def decrypt_data(self, encrypted_data):
        # Decrypt the data
        decrypted_data = self.cipher.decrypt(encrypted_data)
        return decrypted_data.decode('utf-8')