import time
from datetime import datetime, timedelta
import json
from pathlib import Path

from database import (
    get_pending_emails,
    update_status,
    update_attachment_details,
    create_next_recurring_email
)

from attachment_manager import archive_file

from monitoring.monitoring_service import generate_monitoring_report

from smtp import send_email


BASE_DIR = Path(__file__).parent

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
            status = email[6]
            error = email[7]
            attachments = json.loads(email[8]) if email[8] else []
            end_date = email[9]
            repeat_interval = email[10]
            attach_document = email[11]
            attachment_path = email[12]
            attachment_filename = email[13]
            attachment_status = email[14]
            max_occurrences = email[15]
            occurrence_count = email[16]
            actual_attachment_path = None

            print("-------------------------")
            print("Email ID :", email_id)
            print("Database Date :", date)
            print("Database Time :", scheduled_time)

            try:
                scheduled_datetime = datetime.strptime(
                date + " " + scheduled_time,
                    "%d-%m-%Y %H:%M"
                )

            except Exception as e:

                print(
                    "Invalid scheduled date/time:",
                    e
                )

                update_status(
                    email_id,
                    "Failed",
                    f"Invalid scheduled date/time: {str(e)}"
                )

                continue
            
            if  current_datetime < scheduled_datetime:
                continue
            
            try:

                # Automatic Report Attachment
                if attach_document:

                    try:

                        print(
                            "Generating new monitoring report..."
                        )

                        actual_attachment_path = (
                            generate_monitoring_report()
                        )

                        print(
                            "Generated monitoring report:",
                            actual_attachment_path
                        )

                        if not actual_attachment_path:

                            raise FileNotFoundError(
                                "Monitoring report could not be generated."
                            )

                        actual_attachment_path = Path(
                            actual_attachment_path
                        )

                        if not actual_attachment_path.exists():

                            raise FileNotFoundError(
                                f"Generated report does not exist: "
                                f"{actual_attachment_path}"
                            )

                        attachments.append(
                            actual_attachment_path
                        )

                        print(
                            "Attachments being sent:",
                            attachments
                        )

                    except Exception as e:

                        print(
                            "Monitoring report generation error:",
                            e
                        )

                        update_status(
                            email_id,
                            "Failed",
                            f"Monitoring Report Error: {str(e)}"
                        )

                        continue

                # SEND EMAIL
                send_email(
                    recipient,
                    subject,
                    message,
                    attachments
                )

                update_status(
                    email_id,
                    "Sent",
                    None
                )

                print(
                    "Email Sent Successfully"
                )

                # ARCHIVE AUTOMATIC REPORT
                if (
                    attach_document
                    and actual_attachment_path
                ):

                    try:

                        update_attachment_details(
                            email_id,
                            str(actual_attachment_path),
                            actual_attachment_path.name,
                            "Automatic"
                        )

                        archive_file(
                            actual_attachment_path
                        )

                        print(
                            "Monitoring report archived:",
                            actual_attachment_path.name
                        )

                    except Exception as e:

                        print(
                            "Report archive error:",
                            e
                        )

                        # Email was already successfully sent.
                        # Do NOT mark the email as Failed.
                        print(
                            "WARNING: Email was sent, "
                            "but report archival failed."
                        )

                # RECURRING EMAIL LOGIC
                if repeat_interval and repeat_interval != "Never":

                    try:

                        # Check Max Occurrences   
                        if max_occurrences and occurrence_count >= max_occurrences:
                            print("Repeat stopped: Maximum occurrences reached")
                            continue

                        # Calculating next occurrence   
                        if repeat_interval == "Hourly":
                            next_datetime = scheduled_datetime + timedelta(hours=1)

                        elif repeat_interval == "Daily":
                            next_datetime = scheduled_datetime + timedelta(days=1)

                        elif repeat_interval == "Weekly":
                            next_datetime = scheduled_datetime + timedelta(weeks=1)

                        else:
                            print("Unknown repeat interval:", repeat_interval)

                            continue

                        # Check End Date
                        if end_date:
                            end_datetime = datetime.strptime(
                                end_date + " 23:59",
                                "%d-%m-%Y %H:%M"
                            )

                            if next_datetime > end_datetime:
                                print("Repeat stopped: End date reached")

                                continue
    
                        # Create next email
                        new_email_id = (
                            create_next_recurring_email(
                                email,
                                None,
                                None,
                                None,
                                next_datetime.strftime("%d-%m-%Y"),
                                next_datetime.strftime("%H:%M"),
                                occurrence_count + 1
                            )
                        )    

                        print(
                            "Next recurring email created. ID:",
                            new_email_id
                        )
                        print(email)
                        print(new_email_id)

                    except Exception as e:

                        print("Recurring Creation Error (Scheduler Error):", e)
                        update_status(email_id, "Failed", f"Recurring Creation Error: {str(e)}" )

            except Exception as e:

                print("Email Sending Error:", e)
                update_status(email_id, "Failed", str(e))
                print("Email Sending Failed")
                
        time.sleep(30)

if __name__ == "__main__":
    scheduler()
    