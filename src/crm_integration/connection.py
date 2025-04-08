class ConnectionManager:
    def __init__(self):
        self.connection = None
        self.authenticated = False
        self.session = None

    def establish_connection(self):
        """
        Establishes a connection.
        This is a placeholder for actual connection logic.
        """
        if self.connection is None:
            # Placeholder for connection logic
            self.connection = "Connected"
            print("Connection established.")
        else:
            print("Connection already established.")

    def authenticate(self, credentials):
        """
        Authenticates the user with the given credentials.
        This is a placeholder for actual authentication logic.
        """
        if not self.authenticated:
            # Placeholder for authentication logic
            if credentials == "valid_credentials":
                self.authenticated = True
                print("Authentication successful.")
            else:
                print("Authentication failed.")
        else:
            print("Already authenticated.")

    def start_session(self):
        """
        Starts a session if authenticated.
        This is a placeholder for actual session management logic.
        """
        if self.authenticated and self.session is None:
            # Placeholder for session start logic
            self.session = "Session started"
            print("Session started.")
        elif not self.authenticated:
            print("Cannot start session without authentication.")
        else:
            print("Session already started.")

    def close_connection(self):
        """
        Closes the connection.
        This is a placeholder for actual disconnection logic.
        """
        if self.connection is not None:
            # Placeholder for disconnection logic
            self.connection = None
            self.authenticated = False
            self.session = None
            print("Connection closed.")
        else:
            print("No connection to close.")