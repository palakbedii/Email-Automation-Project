import sqlite3
import json
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
        end_date TEXT,
        time TEXT,
        status TEXT,
        error TEXT,
        attachments TEXT,
        repeat_interval TEXT,
        attach_document INTEGER,
        attachment_path TEXT,
        attachment_filename TEXT,
        attachment_status TEXT,
        max_occurrences INTEGER,
        occurrence_count INTEGER DEFAULT 1
    )
    """)

    conn.commit()
    conn.close()

def send_to_sql(
    data,
    attachment_path=None,
    attachment_filename=None,
    attachment_status=None
):

    conn = sqlite3.connect("emails.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO emails(
        recipient,
        subject,
        message,
        date,
        end_date,
        time,
        status,
        attachments,
        repeat_interval,
        attach_document,
        attachment_path,
        attachment_filename,
        attachment_status,
        max_occurrences,
        occurrence_count
    )
    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    """,
    (
        data.recipient,
        data.subject,
        data.message,
        data.date.strftime("%d-%m-%Y"),
        data.end_date.strftime("%d-%m-%Y")
        if data.end_date else None,
        data.time.strftime("%H:%M"),
        "Pending",
        json.dumps(data.attachments),
        data.repeat_interval,
        int(getattr(data, "attach_document", False)),
        attachment_path,
        attachment_filename,
        attachment_status,
        data.max_occurrences,
        1
    ))

    print("Email saved successfully!")
    print(data)

    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return new_id


    # Creates the next recurring row.
    # `next_date` / `next_time` MUST already be the correctly
    # calculated next occurrence (current scheduled time + interval),
    # computed by the caller (scheduler). This function does not
    # do any date math itself.

    # `next_occurrence_count` carries forward how many times this
    # chain has now sent (including the one just sent), so the
    # scheduler can compare it against max_occurrences on the next
    # row too.

def create_next_recurring_email(
    email,
    next_date,
    next_time,
    next_occurrence_count
):
    
    conn = sqlite3.connect("emails.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO emails(
        recipient,
        subject,
        message,
        date,
        end_date,
        time,
        status,
        error,
        attachments,
        repeat_interval,
        attach_document,
        attachment_path,
        attachment_filename,
        attachment_status,
        max_occurrences,
        occurrence_count
    )
    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    """,
    (
        email[1],      # recipient
        email[2],      # subject
        email[3],      # message
        next_date,     # new date
        email[9],      # end_date
        next_time,     # new time
        "Pending",     # new status
        None,          # error
        email[8],      # attachments
        email[10],     # repeat_interval
        email[11],     # attach_document
        email[12],     # attachment_path
        email[13],     # attachment_filename
        email[14],     # attachment_status
        email[15],     # max_occurrences
        next_occurrence_count
    ))

    new_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return new_id


def update_attachment_details(
    email_id,
    attachment_path,
    attachment_filename,
    attachment_status
):

    conn = sqlite3.connect("emails.db")
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE emails
    SET attachment_path=?, attachment_filename=?, attachment_status=?
    WHERE id=?
    """,
    (attachment_path, attachment_filename, attachment_status, email_id))

    conn.commit()
    conn.close()


def save_email(data, status, error=None):

    conn = sqlite3.connect("emails.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO emails(recipient, subject, message, date, time, status, error, attachments)
    VALUES(?,?,?,?,?,?,?,?)
    """, (
        data.recipient,
        data.subject,
        data.message,
        datetime.now().strftime("%d-%m-%Y"),
        datetime.now().strftime("%H:%M"),
        status,
        error,
        json.dumps(data.attachments)
        )
    )

    conn.commit()
    conn.close()

def get_pending_emails():

    conn = sqlite3.connect("emails.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM emails
        WHERE status='Pending'
        ORDER BY id DESC
        """
    )

    emails = cursor.fetchall()

    print("Pending Emails:", emails)

    conn.close()
    return emails


def update_status(email_id, status, error=None):

    conn = sqlite3.connect("emails.db")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE emails
        SET status=?, error=?
        WHERE id=?
    """, (status, error, email_id))

    conn.commit()
    conn.close()

def email_to_dict(email):

    # 0 → id
    # 1 → recipient
    # 2 → subject
    # 3 → message
    # 4 → date
    # 5 → time
    # 6 → status
    # 7 → error
    # 8 → attachments
    # 9 → end_date
    # 10 → repeat_interval
    # 11 → attach_document
    # 12 → attachment_path
    # 13 → attachment_filename
    # 14 → attachment_status
    # 15 → max_occurrences
    # 16 → occurrence_count

    return {
        "id": email[0],
        "recipient": email[1],
        "subject": email[2],
        "message": email[3],
        "date": email[4],
        "time": email[5],
        "status": email[6],
        "error": email[7],
        "attachments": json.loads(email[8]) if email[8] else [],
        "end_date": email[9],
        "repeat_interval": email[10],
        "attach_document": email[11],
        "attachment_path": email[12],
        "attachment_filename": email[13],
        "attachment_status": email[14],
        "max_occurrences": email[15],
        "occurrence_count": email[16]
    }

def store_to_sql(template_data):

    conn = sqlite3.connect("templates.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS templates (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        subject TEXT NOT NULL,
        body TEXT NOT NULL,
        last_edited TEXT
    );
    """)

    cursor.execute("""
    INSERT INTO templates(name, subject, body, last_edited)
    VALUES(?,?,?,?)
    """, (
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
    SELECT *
    FROM templates
    WHERE id = ?
    """, (id,))

    get_template = cursor.fetchone()

    conn.close()
    return get_template

def get_all_templates():

    conn = sqlite3.connect("templates.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM templates
    ORDER BY id
    """)

    templates = cursor.fetchall()

    conn.close()
    return [dict(template) for template in templates]

def search_templates(keyword):

    conn = sqlite3.connect("templates.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM templates
    WHERE
        name LIKE ?
        OR subject LIKE ?
        OR body LIKE ?
    """, (
        f"%{keyword}%",
        f"%{keyword}%",
        f"%{keyword}%"
    ))

    result = cursor.fetchall()

    conn.close()
    return [dict(template) for template in result]

def delete_template(id):

    conn = sqlite3.connect("templates.db")
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM templates
    WHERE id=?
    """,(id,))

    conn.commit()
    conn.close()

def update_template(template_data, id):

    conn = sqlite3.connect("templates.db")
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE templates
    SET
        name=?,
        subject=?,
        body=?,
        last_edited=?
    WHERE id=?
    """, (
        template_data.name,
        template_data.subject,
        template_data.body,
        template_data.last_edited,
        id
    ))

    conn.commit()
    conn.close()


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

    cursor.execute(
        """
        SELECT *
        FROM emails
        WHERE status='Sent'
        ORDER BY id DESC
        """
    )

    emails = cursor.fetchall()

    print("Sent emails are", emails)

    conn.close()
    return emails

def get_failed_emails():

    conn = sqlite3.connect("emails.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM emails
        WHERE status='Failed'
        ORDER BY id DESC
        """
    )

    emails = cursor.fetchall()

    print("Failed emails are", emails)

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