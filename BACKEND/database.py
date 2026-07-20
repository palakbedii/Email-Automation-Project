import sqlite3
from datetime import datetime
from security import encrypt

def create_email_table():

    conn = sqlite3.connect("emails.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS emails(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        recipient TEXT,
        subject TEXT,
        message TEXT,
        date TEXT,
        time TEXT,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()

def send_to_sql(data):

    conn = sqlite3.connect("emails.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO emails(recipient, subject, message, date, time, status)
    VALUES(?,?,?,?,?,?)
    """,
    (
        data.recipient,
        data.subject,
        data.message,
        data.date.strftime("%d-%m-%Y"),
        data.time.strftime("%H:%M"),
        "Pending"
    ))

    print("Email saved successfully!")
    print(data)

    conn.commit()
    conn.close()


def get_pending_emails():

    conn = sqlite3.connect("emails.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM emails
    WHERE status='Pending'
    """)

    emails = cursor.fetchall()

    print("Pending Emails:", emails)

    conn.close()
    return emails


def update_status(email_id):

    conn = sqlite3.connect("emails.db")
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE emails
    SET status='Sent'
    WHERE id=?
    """, (email_id,))

    conn.commit()
    print(f"Email {email_id} marked as Sent")
    conn.close()


def update_status_failed(email_id):

    conn = sqlite3.connect("emails.db")
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE emails
    SET status='Failed'
    WHERE id=?
    """, (email_id,))

    conn.commit()
    print(f"Email {email_id} marked as Failed")
    conn.close()


def store_to_sql(template_data):

    conn = sqlite3.connect("templates.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS templates(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        subject TEXT NOT NULL,
        body TEXT NOT NULL,
        last_edited TEXT NOT NULL
    )
    """)

    cursor.execute("""
    INSERT INTO templates(id, name, subject, body, last_edited)
    VALUES(?,?,?,?,?)
    """, (
        template_data.id,
        template_data.name,
        template_data.subject,
        template_data.body,
        template_data.last_edited
    ))

    conn.commit()
    conn.close()


def retrieve_templates(id):

    conn = sqlite3.connect("templates.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT subject, body
    FROM templates
    WHERE id = ?
    """, (id,))

    get_template = cursor.fetchone()

    conn.close()
    return get_template


def failed_emails_count():

    conn = sqlite3.connect("emails.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT COUNT(status)
    FROM emails
    WHERE status='Failed'
    """)

    failed = cursor.fetchone()[0]

    conn.close()
    return failed


def sent_emails_count():
    conn = sqlite3.connect("emails.db")
    cursor = conn.cursor()

    cursor.execute("""SELECT COUNT(status) FROM emails 
                   WHERE STATUS = 'Sent'
                   """ )
    sent = cursor.fetchone()[0]

    conn.close()
    return sent


def get_sent_emails():
    conn = sqlite3.connect("emails.db")
    cursor = conn.cursor()

    cursor.execute("""SELECT * FROM emails
                WHERE STATUS = 'Sent'
    """)

    emails = cursor.fetchall()

    print("Sent emails are", emails)

    conn.close()
    return emails

def get_totalemails_count():

        conn = sqlite3.connect("emails.db")
        cursor = conn.cursor()

        cursor.execute("""SELECT COUNT(recipient) FROM emails """)

        total_emails = cursor.fetchone()[0]

        conn.close()
        return total_emails


def scheduled_emails_count():
    conn = sqlite3.connect("emails.db")
    cursor = conn.cursor()

    cursor.execute("""SELECT COUNT(status) FROM emails
                    WHERE STATUS = 'Pending'
    """)

    scheduled_emails = cursor.fetchone()[0]
   
    conn.close()
    return scheduled_emails

def get_allemails():
    conn = sqlite3.connect("emails.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM emails")
    rows = cursor.fetchall()

    conn.close()
    return rows


def create_smtp_table():

    conn = sqlite3.connect("emails.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS smtp_settings(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        smtp_host TEXT NOT NULL,
        smtp_port INTEGER NOT NULL,
        sender_email TEXT NOT NULL,
        app_password TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()

def save_smtp_settings(host, port, email, password):

    conn = sqlite3.connect("emails.db")
    cursor = conn.cursor()

    encrypted_password = encrypt(password)

    print("Original password:", password)
    print("Encrypted password:", encrypted_password)

    created_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    cursor.execute("""
    INSERT INTO smtp_settings(
        smtp_host,
        smtp_port,
        sender_email,
        app_password,
        created_at
    )
    VALUES (?, ?, ?, ?, ?)
    """, (
        host,
        port,
        email,
        encrypted_password,
        created_at
    ))

    conn.commit()
    conn.close()
    
def get_smtp_settings():

    conn = sqlite3.connect("emails.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM smtp_settings
    ORDER BY id DESC
    LIMIT 1
    """)

    settings = cursor.fetchone()
    conn.close()
    return settings