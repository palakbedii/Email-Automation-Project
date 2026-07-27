import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from security import decrypt
import database


def send_email(recipient, subject, message, attachments=None):

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
    msg = MIMEMultipart()

    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recipient
    
    msg.attach(MIMEText(message, "plain"))

    if attachments:
        print("Attachments:", attachments)

        for path in attachments:
            path = os.path.abspath(path)

            print("Absolute Path:", path)
            print("Exists:", os.path.exists(path))

            if os.path.exists(path):
                print("Attaching File:", path)
                with open(path, "rb") as file:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(file.read())

                encoders.encode_base64(part)
                part.add_header(
                    "Content-Disposition",
                    f'attachment; filename="{os.path.basename(path)}"'
                )
                msg.attach(part)
                print("Attachment added!")

            else:
                print("File NOT found!")

    try:

        # Connect to SMTP server
        server = smtplib.SMTP(
            smtp_host,
            int(smtp_port)
        )

        server.ehlo()
        server.starttls()
        server.ehlo()

        # Login
        server.login(
            sender,
            password
        )

        # Send email
        server.sendmail(
            sender,
            recipient,
            msg.as_string()
        )

        # Close connection
        server.quit()

    except smtplib.SMTPAuthenticationError:

        raise Exception(
            "SMTP Authentication Failed. "
            "Please check your email and app password."
        )

    except smtplib.SMTPConnectError:

        raise Exception(
            "Unable to connect to SMTP server."
        )

    except smtplib.SMTPRecipientsRefused:

        raise Exception(
            "Recipient email address was rejected."
        )

    except Exception as e:

        raise Exception(
            str(e)
        )