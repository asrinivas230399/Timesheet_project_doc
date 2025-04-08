import hashlib

class DataPrivacy:
    def __init__(self):
        pass

    def anonymize_data(self, data):
        """
        Anonymize data by hashing it.
        :param data: The data to be anonymized.
        :return: Anonymized data.
        """
        if isinstance(data, str):
            data = data.encode('utf-8')
        return hashlib.sha256(data).hexdigest()

    def pseudonymize_data(self, data, key):
        """
        Pseudonymize data using a reversible transformation.
        :param data: The data to be pseudonymized.
        :param key: A key for the pseudonymization process.
        :return: Pseudonymized data.
        """
        pseudonymized_data = ''.join(chr((ord(char) + key) % 256) for char in data)
        return pseudonymized_data

    def depseudonymize_data(self, pseudonymized_data, key):
        """
        Reverse the pseudonymization process to retrieve the original data.
        :param pseudonymized_data: The pseudonymized data.
        :param key: The key used for the pseudonymization process.
        :return: Original data.
        """
        original_data = ''.join(chr((ord(char) - key) % 256) for char in pseudonymized_data)
        return original_data