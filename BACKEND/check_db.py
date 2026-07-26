import sqlite3
import os

print("Database:", os.path.abspath("emails.db"))

conn = sqlite3.connect("emails.db")
cursor = conn.cursor()

cursor.execute("""
SELECT id, subject, recipient, date, time, status
FROM emails
WHERE subject = 'Game';
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()


# import sqlite3

# conn = sqlite3.connect("emails.db")
# cursor = conn.cursor()

# cursor.execute("DELETE FROM emails WHERE id = ?", (15,))

# conn.commit()
# conn.close()

# print("Deleted successfully!")