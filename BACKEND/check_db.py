import sqlite3

conn = sqlite3.connect("emails.db")
cursor = conn.cursor()

cursor.execute("""
SELECT id, subject, date, time, status, repeat_interval, occurrence_count
FROM emails
ORDER BY id DESC
""")

for row in cursor.fetchall():
    print(row)

conn.close()