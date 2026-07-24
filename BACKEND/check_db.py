import sqlite3

conn = sqlite3.connect("emails.db")
cursor = conn.cursor()

# cursor.execute("PRAGMA table_info(emails);")

# columns = cursor.fetchall()

# for column in columns:
#     print(column)

cursor.execute('''SELECT id, recipient, status, error
FROM emails
ORDER BY id DESC;''')

conn.commit()
conn.close()