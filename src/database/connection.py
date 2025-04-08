import sqlite3
from contextlib import contextmanager

DATABASE = 'app.db'

@contextmanager
def get_db_connection():
    """Context manager for database connection."""
    connection = sqlite3.connect(DATABASE)
    try:
        yield connection
    finally:
        connection.close()


def init_db():
    """Initialize the database with necessary tables."""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        # Create users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id TEXT PRIMARY KEY,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                role TEXT NOT NULL
            )
        ''')
        # Create roles table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS roles (
                role_id TEXT PRIMARY KEY,
                role_name TEXT NOT NULL,
                permissions TEXT NOT NULL
            )
        ''')
        conn.commit()


def get_db_session():
    """Get a new database session."""
    return get_db_connection()