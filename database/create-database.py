import sqlite3
import os

# Define the database file path
db_path = os.path.join("database\\face_recognition.db")

# Connect to the SQLite database (it will create the file if it doesn't exist)
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

# Create a table for storing face data
cursor.execute('''
CREATE TABLE IF NOT EXISTS faces (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    face_encoding TEXT NOT NULL
)
''')

# Commit changes and close the connection
connection.commit()
connection.close()

print(f"Database created successfully at {db_path}")


