def authenticate_user(username: str, password: str) -> bool:
    """
    Authenticates a user based on username and password.
    Returns True if authentication is successful, False otherwise.
    """
    # Simulated authentication logic
    return username == "admin" and password == "password"