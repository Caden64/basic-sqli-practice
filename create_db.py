#!/usr/bin/env python3

import sqlite3

DB_PATH = "query.db"

users = [
    ("admin", "admin@example.com", "admin123"),
    ("alice", "alice@example.com", "password123"),
    ("bob", "bob@example.com", "password123"),
]

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
)
""")

cursor.executemany("""
INSERT INTO users (username, email, password)
VALUES (?, ?, ?)
""", users)

conn.commit()
conn.close()

print("users.db populated")
