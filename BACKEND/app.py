from fastapi import FastAPI

from models import (
    EmailRequest,
    TemplateRequest,
    SMTPRequest
)

from database import (
    send_to_sql,
    get_pending_emails,
    store_to_sql,
    retrieve_templates,
    get_sent_emails,
    get_allemails,
    scheduled_emails_count,
    get_totalemails_count,
    sent_emails_count,
    failed_emails_count,
    create_smtp_table,
    save_smtp_settings,
    get_smtp_settings
)

app = FastAPI()

create_smtp_table()


@app.post("/emails")
def schedule(data: EmailRequest):

    send_to_sql(data)

    print("EMAIL RECEIVED")
    print(data)

    return {
        "message": "Email Scheduled Successfully"
    }


@app.get("/emails")
def callallemails():

    all_emails = get_allemails()
    total_emails = get_totalemails_count()

    return {
        "emails": all_emails,
        "total_emails": total_emails
    }


@app.get("/emails/sent")
def callsent_emails():

    sent = get_sent_emails()
    sent_count = sent_emails_count()

    return {
        "emails": sent,
        "sent_count": sent_count
    }


@app.get("/emails/scheduled")
def callpendingemails():

    pending_emails = get_pending_emails()
    scheduled_count = scheduled_emails_count()

    return {
        "emails": pending_emails,
        "scheduled_count": scheduled_count
    }


@app.get("/emails/failed/count")
def get_failed_count():

    failed_count = failed_emails_count()

    return {
        "failed_count": failed_count
    }


@app.post("/templates")
def store_templates(template_data: TemplateRequest):

    store_to_sql(template_data)

    return {
        "message": "Templates saved successfully"
    }


@app.get("/templates/{id}")
def get_stored_templates(id: int):

    get_template = retrieve_templates(id)

    return {
        "subject": get_template[0],
        "body": get_template[1]
    }


@app.post("/smtp_settings")
def save_settings(data: SMTPRequest):

    save_smtp_settings(
        data.smtp_host,
        data.smtp_port,
        data.sender_email,
        data.app_password
    )

    return {
        "message": "SMTP Settings Saved Successfully"
    }


@app.get("/smtp_settings")
def get_settings():

    settings = get_smtp_settings()

    if settings is None:
        return {}

    return {
        "smtp_host": settings[1],
        "smtp_port": settings[2],
        "sender_email": settings[3],
        "app_password": settings[4]
    }