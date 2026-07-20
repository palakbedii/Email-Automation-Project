from datetime import date, time
from pydantic import BaseModel
from pydantic import EmailStr

class EmailRequest(BaseModel):
    recipient: EmailStr
    subject: str
    message: str
    date: date
    time: time

class TemplateRequest(BaseModel):
    id: int
    name: str
    subject: str
    body: str
    last_edited: str

class SMTPRequest(BaseModel):
    smtp_host: str
    smtp_port: int
    sender_email: str
    app_password: str