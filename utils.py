def load_config(file_path: str) -> dict:
    """
    Loads configuration settings from a file.
    Used by main.py to configure the application.
    """
    # Simulated config loading
    return {'data_path': 'data.csv'}

def log(message: str):
    """
    Logs messages to a console or file.
    Used across various modules for logging purposes.
    """
    print(message)