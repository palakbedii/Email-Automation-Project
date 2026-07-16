import smtplib
from email.mime.text import MIMEText
def send_email(recipient, subject, message):
        
        sender = "YOUR_USER_ID"
        password = "YOUR_GMAIL_APP_PASSWORD"

        msg = MIMEText(message) 

        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = recipient

        server = smtplib.SMTP("smtp.gmail.com", 587)

        server.ehlo()

        server.starttls()

        server.ehlo()

        server.login(sender, password)

        server.sendmail(sender, recipient, msg.as_string())

        server.quit()