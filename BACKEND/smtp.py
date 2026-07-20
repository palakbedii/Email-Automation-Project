import smtplib
from email.mime.text import MIMEText
from security import decrypt
import database


def send_email(recipient, subject, message):

    # Get SMTP settings from database
    settings = database.get_smtp_settings()

    if settings is None:
        raise Exception(
            "SMTP settings not found. Please configure SMTP Settings first."
        )

    print("SMTP Settings:", settings)

    # Unpack the database row
    if len(settings) == 6:
        _, smtp_host, smtp_port, sender, encrypted_password, created_at = settings
    elif len(settings) == 5:
        _, smtp_host, smtp_port, sender, encrypted_password = settings
    else:
        raise Exception(f"Unexpected SMTP settings format: {settings}")

    # Decrypt ONLY the password
    password = decrypt(encrypted_password)

    # Create email
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recipient

    # Connect to SMTP server
    server = smtplib.SMTP(smtp_host, int(smtp_port))

    server.ehlo()
    server.starttls()
    server.ehlo()

    # Login
    server.login(sender, password)

    # Send email
    server.sendmail(
        sender,
        recipient,
        msg.as_string()
    )

    # Close connection
    server.quit()