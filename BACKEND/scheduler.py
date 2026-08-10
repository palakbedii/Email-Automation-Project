import time
from datetime import datetime, timedelta
import json
from pathlib import Path

from database import (
    get_pending_emails,
    update_status,
    update_attachment_details,
    create_next_recurring_email,
)

from attachment_manager import (
    get_automatic_attachment,
    resolve_next_attachment,
    archive_file,
    resolve_attachment_path,
)

from smtp import send_email


BASE_DIR = Path(__file__).parent


def calculate_next_datetime(scheduled_datetime, repeat_interval):
    if repeat_interval == "Hourly":
        return scheduled_datetime + timedelta(hours=1)

    elif repeat_interval == "Daily":
        return scheduled_datetime + timedelta(days=1)

    elif repeat_interval == "Weekly":
        return scheduled_datetime + timedelta(weeks=1)

    else:
        try:
            minutes = int(repeat_interval)

            if minutes >= 15:
                return scheduled_datetime + timedelta(minutes=minutes)

        except ValueError:
            return None

    return None


def scheduler():
    print("Scheduler Started")

    while True:
        emails = get_pending_emails()
        print("Checking database...")

        current_datetime = datetime.now()

        print(
            "Current Date:",
            current_datetime.strftime("%d-%m-%Y"),
        )
        print(
            "Current Time:",
            current_datetime.strftime("%H:%M"),
        )

        for email in emails:
            email_id = email[0]
            recipient = email[1]
            subject = email[2]
            message = email[3]
            date = email[4]
            end_date = email[5]
            scheduled_time = email[6]
            status = email[7]
            error = email[8]
            attachments = json.loads(email[9]) if email[9] else []

            resolved_attachments = []

            for attachment in attachments:
                resolved_path = resolve_attachment_path(attachment)

                if resolved_path:
                    resolved_attachments.append(str(resolved_path))
                    print(
                        "Manual attachment resolved:",
                        resolved_path,
                    )
                else:
                    print(
                        "Manual attachment NOT found:",
                        attachment,
                    )

            attachments = resolved_attachments
            repeat_interval = email[10]
            attach_document = email[11]
            attachment_path = email[12]
            attachment_filename = email[13]
            attachment_status = email[14]

            actual_attachment_path = None
            next_attachment_before_archive = None

            max_occurrences = email[15]
            occurrence_count = email[16]

            print("-------------------------")
            print("Database Date:", date)
            print("Database Time:", scheduled_time)

            scheduled_datetime = datetime.strptime(
                date + " " + scheduled_time,
                "%d-%m-%Y %H:%M",
            )

            if current_datetime >= scheduled_datetime:
                try:
                    if attach_document:
                        if attachment_path:
                            actual_attachment_path = BASE_DIR / attachment_path
                        else:
                            automatic_report = get_automatic_attachment()
                            print("Automatic report:", automatic_report)

                            if automatic_report:
                                actual_attachment_path = automatic_report

                        if actual_attachment_path:
                            attachments.append(str(actual_attachment_path))
                            print(
                                "Attachments being sent:",
                                attachments,
                            )

                    send_email(
                        recipient,
                        subject,
                        message,
                        attachments,
                    )

                    update_status(email_id, "Sent", None)
                    print("Email Sent Successfully")

                    if attach_document and actual_attachment_path:
                        next_attachment_before_archive = (
                            resolve_next_attachment(
                                Path(actual_attachment_path).name
                            )
                        )

                    if attach_document and actual_attachment_path:
                        update_attachment_details(
                            email_id,
                            str(actual_attachment_path),
                            Path(actual_attachment_path).name,
                            (
                                "Automatic"
                                if not attachment_filename
                                else attachment_status
                            ),
                        )

                        archive_file(Path(actual_attachment_path))

                    if repeat_interval and repeat_interval != "Never":
                        try:
                            if max_occurrences is not None:
                                if occurrence_count >= max_occurrences:
                                    print("Maximum occurrences reached")
                                    continue

                            next_datetime = calculate_next_datetime(
                                scheduled_datetime,
                                repeat_interval,
                            )

                            if next_datetime is None:
                                print(
                                    "Repeat stopped: "
                                    "Invalid repeat interval"
                                )
                                continue

                            if end_date:
                                end_datetime = datetime.strptime(
                                    end_date + " 23:59",
                                    "%d-%m-%Y %H:%M",
                                )

                                if next_datetime > end_datetime:
                                    print(
                                        "Repeat stopped: "
                                        "End date reached"
                                    )
                                    continue

                            if next_attachment_before_archive:
                                new_email_id = (
                                    create_next_recurring_email(
                                        email,
                                        str(
                                            next_attachment_before_archive
                                        ),
                                        next_attachment_before_archive.name,
                                        "Automatic",
                                        next_datetime.strftime(
                                            "%d-%m-%Y"
                                        ),
                                        next_datetime.strftime("%H:%M"),
                                        occurrence_count + 1,
                                    )
                                )
                            else:
                                new_email_id = (
                                    create_next_recurring_email(
                                        email,
                                        None,
                                        None,
                                        None,
                                        next_datetime.strftime(
                                            "%d-%m-%Y"
                                        ),
                                        next_datetime.strftime("%H:%M"),
                                        occurrence_count + 1,
                                    )
                                )

                            print(
                                "Next recurring email created. ID:",
                                new_email_id,
                            )
                            print(email)
                            print(new_email_id)

                        except Exception as e:
                            print(
                                "Recurring Creation Error "
                                "(Scheduler Error):",
                                e,
                            )
                            update_status(
                                email_id,
                                "Failed",
                                str(e),
                            )

                except Exception as e:
                    print("SMTP Error:", e)
                    update_status(
                        email_id,
                        "Failed",
                        str(e),
                    )
                    print("Email Sending Failed")

        time.sleep(30)


if __name__ == "__main__":
    scheduler()
