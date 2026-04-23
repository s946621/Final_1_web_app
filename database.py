import sqlite3

def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

def get_entries_db():
    conn = sqlite3.connect("entries.db")
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
    conn.commit()
    conn.close()

    e_conn = get_entries_db()
    e_conn.execute("""
        CREATE TABLE IF NOT EXISTS entries (
            author TEXT PRIMARY KEY,
            created_on TEXT DEFAULT CURRENT_DATE,
            content TEXT
        )
    """)
    e_conn.commit()
    e_conn.close()