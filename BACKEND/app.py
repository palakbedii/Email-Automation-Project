from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from smtp import send_email

from models import (
    EmailRequest,
    SendNowRequest,
    TemplateRequest,
    SMTPRequest
)

from database import (
    send_to_sql,
    store_to_sql,
    retrieve_templates,
    get_all_templates,
    delete_template,
    update_template,
    search_templates,
    email_to_dict,
    get_pending_emails,
    get_sent_emails,
    get_failed_emails,
    get_allemails,
    save_email,
    get_totalemails_count,
    scheduled_emails_count,
    sent_emails_count,
    failed_emails_count,
    create_smtp_table,
    save_smtp_settings,
    get_smtp_settings
)

app = FastAPI()

create_smtp_table()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5000",
        "http://localhost:5000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/emails")
def schedule(data: EmailRequest):

    send_to_sql(data)

    print("EMAIL RECEIVED")
    print(data)

    return {
        "message": "Email Scheduled Successfully"
    }


@app.post("/emails/send_now")
def send_now(data: SendNowRequest):

    try:
        send_email(
            data.recipient,
            data.subject,
            data.message
        )

        save_email(
            data,
            status="Sent"
        )

        return {
            "message": "Email Sent Successfully"
        }


    except Exception as e:

        save_email(
            data,
            status="Failed",
            error=str(e)
        )

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@app.get("/emails")
def callallemails():

    all_emails = get_allemails()
    total_emails = get_totalemails_count()

    return {
        "emails": all_emails,
        "total_emails": total_emails
    }

@app.get("/dashboard")
def dashboard():
    return {
        "scheduled": scheduled_emails_count(),
        "sent": sent_emails_count(),
        "failed": failed_emails_count(),
        "templates": len(get_all_templates())
    }


@app.get("/emails/scheduled")
def callpendingemails():

    pending = get_pending_emails()

    emails = [
        email_to_dict(email)
        for email in pending
    ]

    return {
        "emails": emails
    }


@app.get("/emails/sent")
def callsent_emails():

    sent = get_sent_emails()

    emails = [
        email_to_dict(email)
        for email in sent
    ]

    return {
        "emails": emails
    }


@app.get("/emails/failed")
def callfailed_emails():

    failed = get_failed_emails()

    emails = [
        email_to_dict(email)
        for email in failed
    ]

    return {
        "emails": emails
    }


@app.post("/templates")
def store_templates(template_data: TemplateRequest):

    store_to_sql(template_data)

    return {
        "message": "Templates saved successfully"
    }

@app.get("/templates/search")
def search_template(keyword: str):

    result = search_templates(keyword)

    return result


@app.get("/templates/{id}")
def get_stored_templates(id: int):

    get_template = retrieve_templates(id)

    return {
        "id": get_template[0],
        "name": get_template[1],
        "subject": get_template[2],
        "body": get_template[3],
        "last_edited": get_template[4]
    }

@app.get("/templates")
def get_templates():

    templates = get_all_templates()
    return templates

@app.delete("/templates/{id}")
def remove_template(id: int):

    delete_template(id)

    return {
        "message": "Template deleted successfully"
    }

@app.put("/templates/{id}")
def edit_template(id: int, template_data: TemplateRequest):

    update_template(template_data, id)

    return {
        "message": "Template updated successfully"
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