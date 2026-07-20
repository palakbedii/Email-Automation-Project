import sqlite3

conn = sqlite3.connect("emails.db")
cursor = conn.cursor()

cursor.execute("""
ALTER TABLE emails
ADD COLUMN created_at TEXT;
""")

conn.commit()
conn.close()
print("created_at column added successfully")