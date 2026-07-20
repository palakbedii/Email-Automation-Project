import time
from datetime import datetime

from database import (
    get_pending_emails,
    update_status,
    update_status_failed
)

from smtp import send_email


def scheduler():
    print("Scheduler Started")
    while True:

        emails = get_pending_emails()
        print("Checking database...")
        
        current_datetime = datetime.now()

        print("Current Date :", current_datetime.strftime("%d-%m-%Y"))
        print("Current Time :", current_datetime.strftime("%H:%M"))

        for email in emails:

            email_id = email[0]
            recipient = email[1]
            subject = email[2]
            message = email[3]
            date = email[4]
            scheduled_time = email[5]
            print("-------------------------")
            print("Database Date :", date)
            print("Database Time :", scheduled_time)
            scheduled_datetime = datetime.strptime(
            date + " " + scheduled_time,
                "%d-%m-%Y %H:%M"
            )
            
            if  current_datetime >= scheduled_datetime:
                try:
                    send_email(recipient, subject, message)

                    update_status(email_id)

                    print("Email Sent Successfully")

                except Exception as e:

                    print("SMTP Error:", e)

                    update_status_failed(email_id)

                    print("Email Sending Failed")
                
        time.sleep(60)

if __name__ == "__main__":
    scheduler()
    