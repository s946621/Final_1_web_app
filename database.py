import sqlite3

def get_db():
    conn = sqlite3.connect("users.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    # Add your new table between lines 15 & 16.
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS entries (
            created_on TEXT DEFAULT CURRENT_DATE PRIMARY KEY,
            content TEXT
        )
    """)
    conn.commit()
    conn.close()