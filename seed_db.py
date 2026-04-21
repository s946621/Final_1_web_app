#!/usr/bin/env python3
# Seed the database with sample data.
# Run this script once with: python seed_db.py

# Once you have seeded your data, you can run sqlite3 users.db in the terminal
# This opens a sqlite3 shell and you can run commands like:
# - .tables to see all tables
# - SELECT * FROM users; to see all users
# - .exit to exit the shell
# *Note: If you try to seed data and get an error about "UNIQUE constraint failed: users.username", it means you have already seeded the database.
# If you need to seed the database again, simply delete the users.db file and run the seed script again.

from database import get_db, init_db, get_entries_db
import bcrypt

def seed_database():
    """Add sample users to the database"""
    init_db()  # Ensure tables are created
    
    conn = get_db()
    e_conn = get_entries_db()
    
    # Sample users with passwords
    sample_users = [
        ("alice", "Password123!"),
        ("bob", "SecurePass456@"),
        ("charlie", "MyPassword789#"),
    ]
    entries = [
        ("alice", "2016-03-24", "I am alice. Nice to meet you."),
        ("bob", "1824-03-31", "Bob me is."),
        ("charlie", "2222-02-22", "CHARLIE!!!!!")
    ]
    
    try:
        for username, password in sample_users:
            hashed_pw = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
            conn.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, hashed_pw)
            )
            print(f"Created user: {username}")

        for author, created_on, content in entries:
            # hashed_pw = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
            e_conn.execute(
                "INSERT INTO entries (author, created_on, content) VALUES (?, ?, ?)",
                (author, created_on, content)
            )
            print(f"Created entry: {author}")
        
        e_conn.commit()
        conn.commit()
        print("\nDatabase seeding complete!")
    
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")
    
    finally:
        conn.close()

if __name__ == "__main__":
    seed_database()
