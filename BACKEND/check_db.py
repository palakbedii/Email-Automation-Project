# ----------------------------------------------------------------------------------------- 
#  import sqlite3

# conn = sqlite3.connect("emails.db")
# cursor = conn.cursor()

# # Delete the record with ID 59
# cursor.execute("DELETE FROM emails WHERE id = ?", (59,))

# # Commit the changes to the database
# conn.commit()

# # Fetch and print the remaining records
# cursor.execute("SELECT * FROM emails")
# for row in cursor.fetchall():
#     print(row)

# conn.close()

# print("Deleted successfully.")

# ----------------------------------------------------------------------------------------- 
# import sqlite3

# conn = sqlite3.connect("emails.db")
# cursor = conn.cursor()

# cursor.execute("""
# SELECT
# id,
# subject,
# date,
# time,
# status,
# attachment_filename,
# occurrence_count
# FROM emails
# ORDER BY id DESC;
# """)

# for row in cursor.fetchall():
#     print(row)

# conn.close()

# ----------------------------------------------------------------------------------------- 