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

from database import get_db, init_db

def seed_database():
    """Add sample users to the database"""
    init_db()  # Ensure tables are created
    
    conn = get_db()

    # create new samples later

if __name__ == "__main__":
    seed_database()