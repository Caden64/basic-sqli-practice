#!/usr/bin/env python3

import sqlite3

conn = sqlite3.connect("query.db")
cursor = conn.cursor()

print("Login")
username = input("What's your username: ")
password = input("what's your password:")

print(type(username))
print(type(password))

query = "SELECT * FROM users WHERE username = " + username + f" AND password = {password} LIMIT 1"
print(type(query))
print(query)


cursor.execute(query)

rows = cursor.fetchall()

conn.close()

print(rows)

