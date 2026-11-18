
import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("ALTER TABLE users ADD COLUMN username TEXT")
cursor.execute("ALTER TABLE users ADD COLUMN password TEXT")

conn.commit()
conn.close()

print("Database updated!")
